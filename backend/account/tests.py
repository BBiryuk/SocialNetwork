from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SignupTestCase(APITestCase):
    url = reverse('signup')

    def test_signup_valid_data(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'username': 'johndoe',
            'password1': 'password123',
            'password2': 'password123',
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'data': 'success'})

    def test_signup_invalid_data(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalidemail',
            'username': '',
            'password1': 'password123',
            'password2': 'password456',
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'data': 'error'})

    def test_signup_missing_data(self):
        data = {
            'first_name': '',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password1': 'password123',
            'password2': 'password123',
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'data': 'error'})
