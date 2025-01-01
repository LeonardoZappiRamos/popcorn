from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class LoginTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.create(
            username="testuser", password="testpassword"
        )

    def test_successful_login(self):
        response = self.client.post(
            "/api/v1/login/",
            {"username": self.test_user.username, "password": "testpassword"},
            format="json",
        )
        token = Token.objects.get(user__username="admin.popcorn")
        print(token)
        print(response.content)
        print(response.status_code)
        self.assertEqual(201, 201)
