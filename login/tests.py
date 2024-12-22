from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model

class LoginActionTests(TestCase):

    def setUp(self):
        # Set up the test client
        self.client = Client()

        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='Mohammed',
            email='ha200410@gmail.com',
            password='mohammed'
        )

        # Mock the MySQL connection and cursor
        self.patcher = patch('login.views.sql.connect')
        self.mock_connect = self.patcher.start()
        self.mock_cursor = self.mock_connect.return_value.cursor.return_value

    def tearDown(self):
        self.patcher.stop()

    def test_loginaction_correct_credentials(self):
        # Set up the post data
        post_data = {
            'email': 'ha200410@gmail.com',
            'password': 'mohammed'
        }
        
        # Mock the database response
        self.mock_cursor.fetchone.return_value = (self.user.id, self.user.email, self.user.password)
        
        # Access the loginaction view with correct credentials
        response = self.client.post(reverse('loginaction'), data=post_data)
        
        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check if it redirects to the home page
        self.assertRedirects(response, reverse('index'))

    def test_loginaction_incorrect_credentials(self):
        # Set up the post data with incorrect password
        post_data = {
            'email': 'ha200410@gmail.com',
            'password': 'wrongpassword'
        }
        
        # Mock the database response
        self.mock_cursor.fetchone.return_value = (self.user.id, self.user.email, self.user.password)
        
        # Access the loginaction view with incorrect credentials
        response = self.client.post(reverse('loginaction'), data=post_data)
        
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the correct template was used
        self.assertTemplateUsed(response, 'error.html')

    def test_loginaction_user_not_found(self):
        # Set up the post data with a non-existent email
        post_data = {
            'email': 'nonexistent@example.com',
            'password': 'testpassword'
        }
        
        # Mock the database response
        self.mock_cursor.fetchone.return_value = None
        
        # Access the loginaction view with non-existent user credentials
        response = self.client.post(reverse('loginaction'), data=post_data)
        
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the correct template was used
        self.assertTemplateUsed(response,'error.html')
