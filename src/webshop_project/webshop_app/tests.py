from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

# Create your tests here.
class LoginTestCase(TestCase):
    def test_a_new(self):
        client = APIClient()
        x=client.login(email='aliba@metropolia.fi', password='1234')
        #token = Token.objects.get(user__email='aliba@metropolia.fi')
        #client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        print("hello",x)
        client.logout()
