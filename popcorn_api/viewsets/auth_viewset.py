from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from popcorn_api.serializers import LoginSerializer

from datetime import timedelta
from django.utils import timezone
from django.conf import settings


def expires_in(token):
    time_elapsed = timezone.now() - token.created
    left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
    return left_time


# token checker if token expired or not
def is_token_expired(token):
    return expires_in(token) < timedelta(seconds=0)


# if token is expired new token will be established
# If token is expired then it will be removed
# and new one with different key will be created
def token_expire_handler(token):
    is_expired = is_token_expired(token)
    if is_expired:
        token.delete()
        token = Token.objects.create(user=token.user)
    return is_expired, token


class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid(raise_exception=True):
            user = authenticate(
                username=serializer.data["username"],
                password=serializer.data["password"],
            )
            if user:
                token, _ = Token.objects.get_or_create(user=user)

                is_expired, token = token_expire_handler(token)
                return Response(
                    {
                        "token": [token.key],
                        "expires": expires_in(token),
                        "Sucsses": "Login SucssesFully",
                    },
                    status=status.HTTP_201_CREATED,
                )
            return Response({"Massage": "Invalid Username and Password"}, status=401)
