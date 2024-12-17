from django.urls import re_path, include, path
from rest_framework import routers
from rest_framework.authtoken import views
from django.contrib.auth import views as auth_views
from popcorn_api.viewsets import UserViewSet, SeguidorViewSet, FeedViewSet, LoginAPIView


router = routers.DefaultRouter()

# Router Registered
# Exemplo: router.register(r'view_name', Viewname)

router.register(r"feed", FeedViewSet, basename="feed")
router.register(r"users", UserViewSet, basename="users")
router.register(r"follows", SeguidorViewSet, basename="follows")

urlpatterns = [
    re_path("api/", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
    path("api/login/", LoginAPIView.as_view()),
]
