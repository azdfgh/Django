from django.contrib import admin
from blog.models import Entrada
from blog.models import Comentario
# Register your models here.

admin.site.register(Entrada)
admin.site.register(Comentario)
