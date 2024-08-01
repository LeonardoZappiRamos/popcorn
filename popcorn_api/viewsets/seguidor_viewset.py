from rest_framework import viewsets, permissions

from popcorn_api.models import Seguidor
from popcorn_api.serializers import SeguidorSerializer


class SeguidorViewSet(viewsets.ModelViewSet):
    serializer_class = SeguidorSerializer
    queryset = Seguidor.objects.all()
    
    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user).all() 