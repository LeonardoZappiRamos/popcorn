from rest_framework import serializers

from popcorn_api.models import Seguidor


class SeguidorSerializer(serializers.ModelSerializer):
    usuario_username = serializers.CharField(source="usuario.username")
    usuario_seguido_username = serializers.CharField(source="usuario_seguido.username")

    class Meta:
        model = Seguidor
        fields = [
            "usuario",
            "usuario_username",
            "usuario_seguido",
            "usuario_seguido_username",
        ]
