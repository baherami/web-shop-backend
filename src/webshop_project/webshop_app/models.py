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

class ProfileFeedItem(models.Model):
    """Profile status update"""
    #creating related model's fields."""
    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        """convert object to string"""
        return self.status_text
