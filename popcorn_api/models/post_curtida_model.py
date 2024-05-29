from django.db import models
from .post_model import Post
from .usuario_model import Usuario


class Curtida(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)