from rest_framework import viewsets, permissions

from django.contrib.auth.models import User
from popcorn_api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )
    