from django.test import TestCase
from rest_framework.authtoken.models import Token


class LoginTest(TestCase):
    def setUp(self):
        pass

    def test_create_token(self):
        token = Token.objects.create(user="leonardo")
        self.assertEqual(token.username, "leonardo")
