from django.urls import re_path, include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# from rest_framework.authtoken import views
# from django.contrib.auth import views as auth_views
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
    # path("api-token-auth/", views.obtain_auth_token),
    # path("api/login/", viewsets.LoginAPIView.as_view()),
    # path("api/v1/login/", viewsets.LoginViewset),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
