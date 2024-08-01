from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('popcorn_api.urls')),
    path('', include('front.urls')),
    path('auth/token/', TokenObtainPairView.as_view(), name='auth_token'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='auth_token_refresh')
]