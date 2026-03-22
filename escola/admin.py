from django.contrib import admin

# Register your models here.

from .models import Escola 

class EscolaAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade",)
    ordering = ("nome", "idade",)
    serach_field = ("nome",)

admin.site.register(Escola, EscolaAdmin)