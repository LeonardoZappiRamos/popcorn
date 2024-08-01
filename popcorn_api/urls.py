from django.urls import re_path, include
from rest_framework import routers

from popcorn_api.viewsets import PostViewSet, UserViewSet, SeguidorViewSet


router = routers.DefaultRouter()

# Router Registered
# Exemplo: router.register(r'view_name', Viewname)

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'users', UserViewSet, basename='users')
router.register(r'seguidor', SeguidorViewSet, basename='seguidor')

urlpatterns = [
    re_path('api/(?P<version>(v1|v2))/', include(router.urls))
]