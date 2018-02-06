# All serializers of this app are here
from rest_framework import serializers

# import models for more functionality of profile APIV
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """ A serializer for user profile objects"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name','address_country', 'password')
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        """create and return a new user"""

        user = models.UserProfile(
        email = validated_data['email'],
        name = validated_data['name'],
        address_country = validated_data['address_country']
        )

        user.set_password(validated_data['password'])

        user.save()

        return user
class ItemSerializer(serializers.ModelSerializer):
    """A serializer for items"""

    class Meta:
        model = models.Item
        fields = ('id', 'user_profile', 'name', 'price', 'created_on')
        extra_kwargs = {'user_profile':{'read_only': True}}
class CartSerializer(serializers.ModelSerializer):
    """ A serializer for cart"""

    class Meta:
        model = models.Cart
        fields = ('id', 'items', 'total_sum', 'created_on', 'is_payed')
        extra_kwargs = {'user_profile':{'read_only' : True},
        'total_sum':{'read_only' : True}, 'is_payed':{'read_only': True}}
