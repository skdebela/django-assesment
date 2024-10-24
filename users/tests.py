from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class UserRegistrationTest(APITestCase):
    def test_user_registration(self):
        url = reverse('rest_register')
        data = {
            'username': 'testuser',
            'password1': 'strongpassword',
            'password2': 'strongpassword',
            'email': 'testuser@example.com',
            'role': 'football_player'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
