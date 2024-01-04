from django.test import TestCase
from authentication.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class TestAuthAPIs(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('authentication:signup')
        self.login_url = reverse('authentication:login')

        # creating a test user to login
        self.user = User.objects.create(
            email = 'ninja@gmail.com',
            first_name= 'Moses',
            last_name = 'Mugoya'
        )


    # test for valid user signup
    def test_valid_user_signup(self):
        data = {
            'first_name': 'Moses',
            'last_name': 'Mugoya',
            'email': 'moses@gmail.com',
            'password': '@Rand0mpassword',
        }

        response = self.client.post(self.signup_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='moses@gmail.com').exists())
    
    # test for invalid user signup
    def test_invalid_user_signup(self):
        data = {
            'first_name': 'Moses',
            'last_name': 'Mugoya',
            'email': 'moses@gmail.com',
            'password': 'nin'
        }

        response = self.client.post(self.signup_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    # test for valid user login
    def test_valid_user_login(self):
        
        self.user.set_password('@rand0mPass')

        self.user.save()

        data = {
            'email':'ninja@gmail.com',
            'password': '@rand0mPass'
        }

        response = self.client.post(self.login_url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_invalid_user_login(self):
        data = {
            'email':'ninja@gmail.com',
            'password': 'ninja'
        }

        response = self.client.post(self.login_url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    
        





