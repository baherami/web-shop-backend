from django.shortcuts import render

# adding view for user profile
from rest_framework.views import APIView
from rest_framework.response import Response

#import for serializers
from . import serializers
from . import models

from . import permissions

#import HTTP status
from rest_framework import status
#adding authentication
from rest_framework.authentication import TokenAuthentication

from rest_framework import filters
# adding viewset
from rest_framework import viewsets

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import DjangoModelPermissions
# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles CRUD for profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # adding token Authentication tuple
    authentication_classes= (TokenAuthentication,)
    # adding permissions
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    """ Checks email and password of a user and return a token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """ User the ObtainToken APIVIEW to validate a user"""

        return ObtainAuthToken().post(request)

class ItemViewSet(viewsets.ModelViewSet):
    """Handles CRUD for feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()
    permission_classes = (permissions.OwnItemChange, DjangoModelPermissions,)

    def create(self, request):
        """ Sets the user profile to the logged in user"""
        serializer = serializers.ItemSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save(user_profile=self.request.user)
            return Response({'Operation': 'Done'})

        else:
            return Response(
            serializer.errors, status = status.HTTP_400_BAD_REQUEST)
