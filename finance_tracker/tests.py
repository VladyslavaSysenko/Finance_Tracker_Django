from . models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status



class UserTestCase(APITestCase):

    """
    Test suite for User
    """
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "username": "Billy",
            "password": "1111",
            "email": "billy@test.com"
        }
        self.url = "/user/"

    def test_create_user(self):
        '''
        test UserViewSet create method
        '''
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "Billy")

    def test_create_user_without_name(self):
        '''
        test userViewSet create method when name is not in data
        '''
        data = self.data
        data.pop("username")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_user_when_name_equals_blank(self):
        '''
        test userViewSet create method when name is blank
        '''
        data = self.data
        data["username"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_password(self):
        '''
        test userViewSet create method when message is not in data
        '''
        data = self.data
        data.pop("password")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_user_when_password_equals_blank(self):
        '''
        test userViewSet create method when message is blank
        '''
        data = self.data
        data["password"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_email(self):
        '''
        test userViewSet create method when email is not in data
        '''
        data = self.data
        data.pop("email")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_user_when_email_equals_blank(self):
        '''
        test userViewSet create method when email is blank
        '''
        data = self.data
        data["email"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_when_email_equals_non_email(self):
        '''
        test userViewSet create method when email is not email
        '''
        data = self.data
        data["email"] = "test"
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)