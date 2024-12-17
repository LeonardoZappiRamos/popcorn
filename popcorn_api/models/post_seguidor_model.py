from django.db import models
from django.contrib.auth.models import User


class Seguidor(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_seguidor"
    )
    usuario_seguido = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_seguido"
    )
