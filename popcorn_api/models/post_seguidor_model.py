from django.db import models
from django.contrib.auth.models import User


class Seguidor(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_seguido = models.ForeignKey(User, on_delete=models.CASCADE)