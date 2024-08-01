from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120, blank=False)
    conteudo = models.TextField(max_length=500)
    data_updated = models.DateTimeField(auto_now=True)
    data_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_created',)