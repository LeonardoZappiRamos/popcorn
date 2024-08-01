from django.contrib import admin

from popcorn_api.models import Post, Curtida, Comentario, Seguidor

# Register your models here.

admin.site.register(Seguidor)
admin.site.register(Post)
admin.site.register(Curtida)
admin.site.register(Comentario)