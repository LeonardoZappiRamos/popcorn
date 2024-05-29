from django.db import models


class Filme(models.Model):
    titulo = models.CharField(max_length=250)
    sinopse = models.TextField()
    data_lanc = models.DateField()
    