from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('login/', views.login, name="Login"),
    path('logout/', views.logout, name="Logout"),
]