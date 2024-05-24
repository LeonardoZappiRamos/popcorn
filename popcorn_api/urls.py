from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

# Router Registered
# Exemplo: router.register(r'view_name', Viewname)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]