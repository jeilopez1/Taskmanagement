from django.test import TestCase
from apps.advanced_task_management.api.services.conection_rick_and_morty import conection_rick_and_morty
from rest_framework.test import APIClient
from rest_framework import status

class RickIsLiveTestCase(TestCase):
    def test_RickIsLive(self):
        instance = conection_rick_and_morty()
        client = APIClient()
        request_data = "character"
        response = instance.RickIsLive(request_data)  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
