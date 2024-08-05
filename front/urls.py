from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('users/', views.users, name="Users"),
    path('login/', views.login, name="Login"),
    path('logout/', views.logout, name="Logout"),
    path('logout/', views.signin, name="SignIn"),
    path('Follow/', views.follow, name="Follow"),
    path('Unfollow/', views.unfollow, name="Unfollow"),
]