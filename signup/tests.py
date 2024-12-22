from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock

class SignupActionTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signupaction')  # Adjust this if your URL name is different

    @patch('signup.views.sql.connect')
    def test_signupaction_post(self, mock_connect):
        # Mock the MySQL connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        # Set up the post data
        post_data = {
            'user_name': 'Mohammed10',
            'first_name': 'Mohammed',
            'last_name': 'Ahmed',
            'email': 'ha200410@gmail.com',
            'password': 'mohammed',
            'phone': '01061761374',
            'address': 'Gardencity',
            'role': 'admin'
        }
        
        # Send POST request
        response = self.client.post(self.signup_url, data=post_data)
        
        # Check the response status
        self.assertEqual(response.status_code, 200)
        # Check if the correct template was used
        self.assertTemplateUsed(response, 'signup_page.html')
        
        # Check if the cursor.execute was called with the expected query
        expected_query = """INSERT INTO users (username, first_name, last_name, email, password, phone_number, address, role) 
                            VALUES ('Mohammed10', 'Mohammed', 'Ahmed', 'ha200410@gmail.com', '{}', '01061761374', 'Gardencity', 'admin')"""
        
        # The hashed password needs to be checked separately due to its dynamic nature
        query_args = mock_cursor.execute.call_args[0][0]
        self.assertIn("INSERT INTO users (username, first_name, last_name, email, password, phone_number, address, role)", query_args)
        self.assertIn("VALUES ('Mohammed10', 'Mohammed', 'Ahmed', 'ha200410@gmail.com',", query_args)
        self.assertIn("'01061761374', 'Gardencity', 'admin')", query_args)

    def test_signupaction_get(self):
        response = self.client.get(self.signup_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup_page.html')
