from django.contrib import admin

# Register your models here.

from .models import Loja

class LojaAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade",)
    ordering = ("nome", "idade",)
    serach_field = ("nome",)

admin.site.register(Loja, LojaAdmin)
