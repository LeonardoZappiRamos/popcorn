from django.urls import re_path, include, path
from rest_framework import routers
from popcorn_api import viewsets


router = routers.DefaultRouter()

# Router Registered
# Exemplo: router.register(r'view_name', Viewname)

router.register(r"feed", viewsets.FeedViewSet, basename="feed")
router.register(r"users", viewsets.UserViewSet, basename="users")
router.register(r"follows", viewsets.SeguidorViewSet, basename="follows")
router.register(r"login", viewsets.LoginViewset, basename="login")

urlpatterns = [
    re_path("api/v1/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
