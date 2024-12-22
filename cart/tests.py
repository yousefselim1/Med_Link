from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
import uuid

class ShoppingCartTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.add_to_cart_url = reverse('add_to_cart')
        self.remove_from_cart_url = reverse('remove_from_cart')
        self.update_cart_url = reverse('update_cart')
        self.view_cart_url = reverse('view_cart')
        self.login_url = reverse('login')

    @patch('cart.views.sql.connect')
    def test_add_to_cart(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        session_key = str(uuid.uuid4())
        self.client.session['session_key'] = session_key

        post_data = {'productId': '1', 'quantity': '2'}
        response = self.client.post(self.add_to_cart_url, data=post_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('view_cart'))

        expected_query = """
            INSERT INTO ShoppingCart (SessionID, DrugID, Quantity) VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE Quantity = Quantity + VALUES(Quantity)
        """
        mock_cursor.execute.assert_called_with(expected_query, (session_key, '1', 2))

    @patch('cart.views.sql.connect')
    def test_remove_from_cart(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        session_key = str(uuid.uuid4())
        self.client.session['session_key'] = session_key

        post_data = {'productId': '1'}
        response = self.client.post(self.remove_from_cart_url, data=post_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('view_cart'))

        expected_query = "DELETE FROM ShoppingCart WHERE SessionID = %s AND DrugID = %s"
        mock_cursor.execute.assert_called_with(expected_query, (session_key, '1'))

    @patch('cart.views.sql.connect')
    def test_update_cart(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        session_key = str(uuid.uuid4())
        self.client.session['session_key'] = session_key

        post_data = {'productId': '1', 'quantity': '3'}
        response = self.client.post(self.update_cart_url, data=post_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('view_cart'))

        expected_query = "UPDATE ShoppingCart SET Quantity = %s WHERE SessionID = %s AND DrugID = %s"
        mock_cursor.execute.assert_called_with(expected_query, (3, session_key, '1'))

    @patch('cart.views.sql.connect')
    def test_view_cart(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        session_key = str(uuid.uuid4())
        self.client.session['session_key'] = session_key

        mock_cursor.fetchall.return_value = [
            ('Drug A', 10.0, 2),
            ('Drug B', 20.0, 1)
        ]

        response = self.client.get(self.view_cart_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

        expected_products = [
            {'name': 'Drug A', 'price': 10.0, 'quantity': 2},
            {'name': 'Drug B', 'price': 20.0, 'quantity': 1}
        ]
        self.assertEqual(response.context['products'], expected_products)

    @patch('cart.views.sql.connect')
    def test_login(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        post_data = {'Mohammed10': 'Mohammed10', 'mohammed': 'mohammed'}
        response = self.client.post(self.login_url, data=post_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'login.html')
