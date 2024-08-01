from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from popcorn_api.models import Post, Seguidor
from popcorn_api.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    
    def get_queryset(self):
        seguidor = Seguidor.objects.values_list("usuario_seguido", flat=True).filter(usuario=self.request.user)
        return super().get_queryset().filter(usuario__id__in=seguidor).all() 
    
    def create(self, request, *args, **kwargs):
        if request.user.id == request.data.get('usuario'):
            return super().create(request, *args, **kwargs)
        else:
            return Response({"message": "Invalid User"}, status=status.HTTP_403_FORBIDDEN)