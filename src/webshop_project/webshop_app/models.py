from django.db import models

#Adding imorts for user models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

#user manager imports for user model
from django.contrib.auth.models import BaseUserManager


#


# Create your models here.
class UserProfileManager(BaseUserManager):
    """django will use this to understand our user model (altered model)"""

    def create_user(self, email, name, password=None):
        """Create and validate a new user profile object"""
        if not email:
            raise ValueError("Email is needed. Please provide it.")
        # standardize the email for all users.
        email = self.normalize_email(email)

        user = self.model(email = email, name = name)
        # assign hashed password to object
        user.set_password(password)
        # saving the user in database
        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password):
        """ create a super user """
        # first we create a normal user with the input data
        user= self.create_user(email, name, password)
        # then we add more power to the user
        user.is_superuser= True
        user.is_staff= True

        # we save the changes to database
        user.save(using=self.db)

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """The override for  user's model as we wish to have in this app"""
    #login credentials for this system, username is user's email in our app
    email = models.EmailField(max_length=255,unique=True)
    #user's name
    name = models.CharField(max_length=255)
    #address for VAT calculations
    address_country =models.CharField(max_length=2)
    # this is for test purpose and a user should not be active by default
    is_active = models.BooleanField(default=True)
    # Both fields, is_active and is_staff are part of django user model
    # and we should override them.
    # is_staff is for administrative reasons, and should be inactive by default
    is_staff = models.BooleanField(default=False)

    #object manager is a class for managing userprofiles, required for override

    objects = UserProfileManager()

    # what django model uses for authentication, override it with email
    USERNAME_FIELD = 'email'
    # list of fields for registration process, only name is applied here
    REQUIRED_FIELDS = ['name']

    # helper functions
    def get_full_name(self):
        """ To get a user's short name"""
        return self.name

    def  get_short_name(self):
        """ This method is called after login so here we have to define it"""
        return self.name

    def _str_(self):
        """convert object to string"""
        return self.name


class Item(models.Model):
    """ Represents an Item that is created by admins, on top of
        the price of the item, depending on which country the order
        comes from, a specific VAT will be added to the item's price. """
    # the admin user who created this item
    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    # item's name
    name = models.CharField(max_length=100)
    # price with two digits for cents, cosidering the shop to use certain-
    # currencies, like euros, dollars or pounds.
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # keeping track of the date that item is created
    created_on = models.DateTimeField(auto_now_add=True)


    # future implementations' fields:
    # normal_price
    # offer_price
    # number_of_items_available
    # producerID
    def _str_(self):
        """convert object to string"""
        return self.name

class Cart(models.Model):
    """ Represent an order of an Item by a User, containing the VAT info"""
    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    is_payed = models.BooleanField(default=True)
    def _str_(self):
        """convert object to string"""
        return "A cart sample"
