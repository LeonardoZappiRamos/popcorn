from rest_framework import serializers

from django.contrib.auth.models import User
from .post_serializer import PostSerializer


class FeedSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fildes = ["id", "posts"]
        read_only = True
