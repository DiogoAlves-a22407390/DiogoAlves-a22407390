from django.contrib import admin

# Register your models here.

from .models import Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade",)
    ordering = ("nome", "idade",)
    serach_field = ("nome",)

admin.site.register(receita, ReceitaAdmin)
