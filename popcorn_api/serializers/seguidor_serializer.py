from rest_framework import serializers

from popcorn_api.models import Seguidor
from django.contrib.auth.models import User


class SeguidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguidor
        fields = ['usuario', 'usuario_seguido']