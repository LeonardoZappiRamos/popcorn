from django.contrib import admin

from .models import Usuario, Post, Filme, Curtida, Comentario, Seguidor

# Register your models here.

admin.site.register(Seguidor)
admin.site.register(Post)
admin.site.register(Curtida)
admin.site.register(Comentario)
# admin.site.register(Filme)