from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialApp



class ViewTests(TestCase):

    def setUp(self):
        # Set up the test client
        self.client = Client()

        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='mohammed',
            email='ha200410@gmail.com',
            password='mohammed'
        )

    def test_index_view_authenticated(self):
        # Log in the user
        self.client.login(username='mohammed', password='mohammed')
        
        # Access the index view
        response = self.client.get(reverse('index'))
        
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the correct template was used
        self.assertTemplateUsed(response, 'home/index.html')

    def test_index_2_view_authenticated(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        
        # Access the index_2 view
        response = self.client.get(reverse('index_2'))
        
        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check if it redirects to the home page
        self.assertRedirects(response, reverse('index'))

    def test_index_2_view_not_authenticated(self):
        # Access the index_2 view without logging in
        response = self.client.get(reverse('index_2'))
        
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the correct template was used
        self.assertTemplateUsed(response, 'login_page.html')

    def test_loginaction_correct_credentials(self):
        # Set up the post data
        post_data = {
            'email': 'ha200410@gmail.com',
            'password': 'mohammed'
        }
        
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
        
        # Access the loginaction view with non-existent user credentials
        response = self.client.post(reverse('loginaction'), data=post_data)
        
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the correct template was used
        self.assertTemplateUsed(response,'error.html')


