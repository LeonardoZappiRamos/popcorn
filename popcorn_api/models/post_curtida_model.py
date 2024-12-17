from django.db import models
from django.contrib.auth.models import User
from .post_model import Post


class Curtida(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
