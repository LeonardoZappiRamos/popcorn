from django.contrib import admin
from django.urls import path, include
from popcorn_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("popcorn_api.urls"), name="api"),
    path("update_server/", views.update, name="update"),
    path("hello/", views.hello_world, name="hello_world"),
]
