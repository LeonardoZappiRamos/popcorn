from django.db import models
from django.contrib.auth.models import User
from .post_model import Post


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=500)
    