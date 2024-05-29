from rest_framework import serializers

from popcorn_api.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = ('usuario', 'filme', 'titulo', 'conteudo', 'data_updated', 'data_created')