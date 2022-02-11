from pydoc import cli
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
# Create your tests here.


class ProductTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username = "test1",password = "test1")
        self.user2 = User.objects.create(username = "test2",password = "test2")
    
    def get_client(self):
        client = APIClient()
        client.login(username = self.user.username,password="test1")
        return client
