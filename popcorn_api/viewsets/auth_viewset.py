from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from popcorn_api.serializers import LoginSerializer
from django.shortcuts import get_object_or_404
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


class LoginViewset(ViewSet):
    permission_classes = [AllowAny]

    def retrieve(self, request, pk: int = None):
        try:
            user = User.objects.get(pk=pk)
            if user:
                queryset = Token.objects.all()
                token = get_object_or_404(queryset, user__id=user.id)
                is_expired = is_token_expired(token)
                if is_expired:
                    return Response(
                        {"message": "Token is expired !!!"},
                        status.HTTP_401_UNAUTHORIZED,
                    )
                return Response(
                    {
                        "token": [token.key],
                        "expires": expires_in(token),
                        "Success": "Login SuccessFully",
                    },
                    status.HTTP_200_OK,
                )
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(
                username=serializer.data["username"],
                password=serializer.data["password"],
            )
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                is_expired, token = token_expire_handler(token)
                response = Response(
                    {
                        "token": [token.key],
                        "user": user.id,
                        "expires": expires_in(token),
                        "message": "Login Successfully",
                    },
                    status=status.HTTP_201_CREATED,
                )
                return response
        return Response({"message": "Invalid Username and Password"}, status=401)
