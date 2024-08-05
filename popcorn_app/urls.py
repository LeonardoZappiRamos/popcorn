from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('popcorn_api.urls'), name="api"),
    path('', include('front.urls'), name="front"),
    path('auth/token/', TokenObtainPairView.as_view(), name='auth_token'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='auth_token_refresh')
]