from django.contrib import admin
from .models import Artigo, Comentario
 
@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')
    search_fields = ('titulo', 'texto')
    list_filter = ('data_criacao',)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'artigo', 'data_criacao')