from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
from django.template.exceptions import TemplateDoesNotExist
from django.shortcuts import render
def payment_view(request):
    try:
        return render(request, 'login_page.html')
    except TemplateDoesNotExist:
        return render(request, 'error.html', {'message': 'Template not found'})

class PaymentViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.session = self.client.session
        self.session['session_key'] = 'test_session_key'
        self.session.save()

    @patch('payment.views.sql.connect')
    def test_payment_view_with_items(self, mock_connect):
        # Mock the database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Set up mock data
        mock_cursor.fetchall.return_value = [
            ('Drug1', 10.0, 2),
            ('Drug2', 20.0, 1)
        ]

        response = self.client.get(reverse('payment_view'))

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check the context data
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 2)
        self.assertEqual(response.context['total'], 40.0)
        self.assertEqual(response.context['shipping'], 20)
        self.assertEqual(response.context['grand_total'], 60.0)

    @patch('payment.views.sql.connect')
    def test_payment_view_without_session_key(self, mock_connect):
        self.client.session.flush()
        response = self.client.get(reverse('payment_view'))

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check if the user is redirected to the login page
        self.assertTemplateUsed(response, 'login_page.html')

    @patch('payment.views.sql.connect')
    def test_payment_view_with_empty_cart(self, mock_connect):
        # Mock the database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Set up mock data
        mock_cursor.fetchall.return_value = []

        response = self.client.get(reverse('payment_view'))

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check the context data
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 0)
        self.assertEqual(response.context['total'], 0)
        self.assertEqual(response.context['shipping'], 20)
        self.assertEqual(response.context['grand_total'], 20.0)

if __name__ == '__main__':
    import unittest
    unittest.main()

class PaymentViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        print(cls.databases)  # Check the value of databases
        super().setUpClass()