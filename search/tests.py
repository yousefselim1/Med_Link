from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock

class SearchDrugsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.search_url = reverse('search_drugs')  # Adjust this if your URL name is different

    @patch('search.views.sql.connect')
    def test_search_drugs_post_with_results(self, mock_connect):
        # Mock the MySQL connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        # Set up the mock cursor's fetchall method
        mock_cursor.fetchall.return_value = [
            (1, 'Aspirin', 'Painkiller', 'Used to reduce pain', 10.0, 'link_to_aspirin'),
            (2, 'Paracetamol', 'Painkiller', 'Used to reduce fever', 5.0, 'link_to_paracetamol')
        ]
        
        # Send POST request with a search query
        response = self.client.post(self.search_url, {'search_query': 'pain'})
        
        # Check the response status
        self.assertEqual(response.status_code, 200)
        # Check if the correct template was used
        self.assertTemplateUsed(response, 'drug_search_results.html')
        # Check if the results are in the context
        self.assertIn('results', response.context)
        # Check if the query is in the context
        self.assertIn('query', response.context)
        # Check the length of the results
        self.assertEqual(len(response.context['results']), 2)
        # Check the content of the results
        self.assertEqual(response.context['results'][0]['name'], 'Aspirin')
        self.assertEqual(response.context['results'][1]['name'], 'Paracetamol')

    @patch('search.views.sql.connect')
    def test_search_drugs_post_no_results(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        # Set up the mock cursor's fetchall method to return no results
        mock_cursor.fetchall.return_value = []
        
        response = self.client.post(self.search_url, {'search_query': 'nonexistentdrug'})
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drug_search_results.html')
        self.assertIn('results', response.context)
        self.assertIn('query', response.context)
        self.assertEqual(len(response.context['results']), 0)

    def test_search_drugs_get(self):
        response = self.client.get(self.search_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drug_search.html')
