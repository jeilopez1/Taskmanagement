from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class RickIsLiveTestCase(TestCase):
    def test_RickIsLive(self):
        client = APIClient()
        request_data = {"endpoint":"character"}
        response = client.post("/api/rickandmorty/",request_data)  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
