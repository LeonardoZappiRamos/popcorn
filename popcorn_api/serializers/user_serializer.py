from rest_framework import serializers

from django.contrib.auth.models import User
from .seguidor_serializer import SeguidorSerializer


class UserSerializer(serializers.ModelSerializer):
    # user_seguido = SeguidorSerializer(many=True)
    user_seguido = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ["id", "username", "user_seguido", "is_active"]
        read_only_fields = ["user_seguido"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
