from rest_framework import serializers

from popcorn_api.models import Post


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="usuario.username", read_only=True) 
    class Meta:
        model = Post
        fields = '__all__'