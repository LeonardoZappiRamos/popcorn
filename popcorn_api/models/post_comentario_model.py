from django.db import models
from .post_model import Post
from .usuario_model import Usuario

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=500)