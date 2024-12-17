from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from popcorn_api.models import Post, Seguidor
from popcorn_api.serializers import PostSerializer


class FeedViewSet(viewsets.ViewSet):
    """ViewSet to list the feed and retrieve the news post"""

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def create(self, request):
        serialized = PostSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(
                data={"message": "Post Created"}, status=status.HTTP_201_CREATED
            )
        return Response(
            data={"message": "Erro creating post"}, status=status.HTTP_400_BAD_REQUEST
        )
