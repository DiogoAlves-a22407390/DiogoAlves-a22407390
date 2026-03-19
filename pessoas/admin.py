from django.contrib import admin

from .models import Pessoa 

class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade",)
    ordering = ("nome", "idade",)
    serach_field = ("nome",)

admin.site.register(Pessoa, PessoaAdmin)

# Register your models here.
