from django.test import TestCase
from rest_framework.test import APIClient
import json


class LoginTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_successful_login(self):
        response = self.client.post(
            "/api/v1/login/",
            {"username": "admin.popcorn", "password": "RNxQw0PQxvYyptcmMraG"},
            format="json",
        )
        print(response.content)
        self.assertEqual(201, 201)
