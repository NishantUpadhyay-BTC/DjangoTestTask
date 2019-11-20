from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from core.models.model_app_users import User
from .serializers import UserSerializers
from rest_framework.authtoken.models import Token
from Multi_Tenant import urls


class UsersTest(APITestCase):
    def setUp(self):
        self.data = {
            "username":'test_11', 
            "email":'test_user@tenant.com',
            "info":{},
            "password":"qwerty@123"
        }
        self.user = self.create_user(self.data)
        self.client = APIClient()
        self.url = reverse('users-list')


    @staticmethod
    def create_user(data):
        user = User.objects.create(**data)
        user.set_password(data['password'])
        user.save()
        return user

    @staticmethod
    def login_user(client, user):
        token = Token.objects.create(user=user)
        client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

    def test_user_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_user_delete(self):
        data = {
            "username" : 'test_delete_user', "password" : 'qwerty@123'
        }
        user = self.create_user(data)
        user_client = APIClient()
        user_client.login(username=data['username'],password=data['password'])
        url = reverse('users-detail', kwargs={"pk": user.id})
        response = user_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
    
    def test_user_delete_without_login_error(self):
        data = {
            "username": 'test_delete_user', "password": 'qwerty@123'
        }
        user = self.create_user(data)
        user_client = APIClient()
        url = reverse('users-detail',kwargs={"pk":user.id})
        response = user_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED,
                         'Expected Response Code 404, received {0} instead.'
                         .format(response.status_code))


    def test_user_delete_no_user_error(self):
        data = {
            "username": 'test_delete_user', "password": 'qwerty@123'
        }
        user = self.create_user(data)
        user_client = APIClient()
        user_client.login(username=data['username'], password=data['password'])
        url = reverse('users-detail', kwargs={"pk": User.objects.last().id+1})
        response = user_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND,
                         'Expected Response Code 404, received {0} instead.'
                         .format(response.status_code))

    

    def test_user_update(self):
        url = reverse('users-detail',kwargs={'pk':self.user.id})
        self.login_user(self.client,self.user)
        response = self.client.put(url,data={'username':'qwerty',"email":"asd@fmail.com"})
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


    def test_user_update_email_username(self):
        self.client.login(username=self.user.username, password="qwerty@123")
        self.login_user(self.client, self.user)
        url = reverse('users-detail', kwargs={"pk": self.user.id})
        response = self.client.put(
            url, data={"email": "tes55t11@gmail.com", "username": "test1555551"})
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_user_update_email_username_error(self):
        self.client.login(username=self.user.username, password="qwerty@123")
        self.login_user(self.client, self.user)
        url = reverse('users-detail', kwargs={"pk": 87})
        response = self.client.put(
            url, data={'username':"qwqwqw"})
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, 'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
