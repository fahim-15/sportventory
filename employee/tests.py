from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class LoginAPITestCase(TestCase):
    def setUp(self):
        """
        Create a user for testing purposes.
        """
        self.client = APIClient()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.login_url = reverse('login')

    def test_login_successful(self):
        """
        Test login with valid credentials.
        """
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIsInstance(response.data['token'], str)

    def test_login_invalid_credentials(self):
        """
        Test login with invalid credentials.
        """
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

    def test_login_missing_fields(self):
        """
        Test login with missing fields.
        """
        response = self.client.post(self.login_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertIn('password', response.data)
