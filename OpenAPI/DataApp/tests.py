from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .schema import DUMMY_DATA

from .models import DummyData #ref purpose, mock simulates for testing purpose
from unittest.mock import patch
from urllib.parse import urlencode



class DummyDataAPITests(APITestCase):
    def setUp(self):
        # Initialize data before tests
        self.list_url = reverse('dummy-data-list')

    def test_list_dummy_data(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['data'], list)
        print("Test case executed ")

    @patch('DataApp.models.DummyData')  
    def test_create_dummy_data(self, MockDummyData):
        # Configure the mock instance
        mock_instance = MockDummyData.return_value
        mock_instance.ten_min_std_deviation = '15'
        mock_instance.time = '2.5'  
        mock_instance.datetime = '2024-12-19T12:34:56'
        mock_instance.ten_min_sampled_avg = '27.8'

        # Simulate the create method
        MockDummyData.objects.create.return_value = mock_instance

        # Perform the API request
        url = reverse('dummy-data-list')
        data = {
            "10_min_std_deviation": "15",
            "time": "2.46",
            "datetime": "2024-12-19T12:34:56",
            "10_min_sampled_avg": "24.8"
        }
        response = self.client.post(url, data, format='json')
        #print(response)
        #print(response.data)
        #print(type(response))

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict) 
        print("Test case executed")


    @patch('DataApp.models.DummyData')
    def test_update_dummy_data(self, MockDummyData):
        # Configure the mock instance
        mock_instance = MockDummyData.return_value
        mock_instance.id = 1
        mock_instance.ten_min_std_deviation = '15'
        mock_instance.time = '2.5'
        mock_instance.datetime = '2024-12-19T12:34:56'
        mock_instance.ten_min_sampled_avg = '27.8'

        # Simulate the get method
        MockDummyData.objects.get.return_value = mock_instance

        # Perform the API request
        url = reverse('dummy-data-detail', args=[mock_instance.id])  
        updated_data = {
            "10_min_std_deviation": "15",
            "time": "2.46",
            "datetime": "2024-12-19T12:34:56",
            "10_min_sampled_avg": "24.8"
        }
        response = self.client.put(url, updated_data, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        print("Test case executed")


    @patch('DataApp.models.DummyData')
    def test_delete_dummy_data(self, MockDummyData):
        # Configure the mock instance
        mock_instance = MockDummyData.return_value
        mock_instance.id = 4

        # Simulate the get method
        MockDummyData.objects.get.return_value = mock_instance

        # Perform the API request
        url = reverse('dummy-data-detail', args=[mock_instance.id])
        response = self.client.delete(url, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("Test case executed")



'''
    @patch('DataApp.models.DummyData')
    def test_retrieve_dummy_data(self, MockDummyData):
        # Configure the mock instance
        mock_instance = MockDummyData.return_value
        mock_instance.id = 1
        mock_instance.ten_min_std_deviation = '17'
        mock_instance.ten_min_sample_avg = '24.8'
        mock_instance.time = '2.5'
        mock_instance.datetime = '2024-12-19T12:34:56'

        # Simulate the get method
        MockDummyData.objects.get.return_value = mock_instance

        # Perform the API request
        #base_url = reverse('dummy-data-list')
        #query_params = {'name': 'Tommy'}
        #full_url = f"{base_url}?{urlencode(query_params)}"
        #print(full_url)
        #url = reverse('dummy-data-list', args=[mock_instance.name])  # Ensure this URL name matches your URL configuration
        url = reverse('dummy-data-list')
        #print(url)
        response = self.client.get(url,{'name': 'John Doe'}, format='json')
        #print(response)
        #print(response.data)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], 'John Doe')
'''
