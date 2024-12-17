from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from popcorn_api.models import Seguidor
from popcorn_api.serializers import SeguidorSerializer


class SeguidorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Seguidor.objects.all()
        serializer = SeguidorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SeguidorSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"message": "Follow Done."}, status=status.HTTP_201_CREATED
            )
        return Response(
            data={"message": "Error in follow."}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, seguidor=None):
        pass
