# This is for adding view to our Hello API
from django.conf.urls import url
# adding include
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('Login', views.LoginViewSet, base_name='login')
urlpatterns = [
    url(r'',include(router.urls)),
]
