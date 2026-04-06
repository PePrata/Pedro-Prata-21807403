from django.contrib import admin

from .models import Licenciatura,Tecnologia

# Register your models here.

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)

admin.site.register(Licenciatura, LicenciaturaAdmin)

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome","logotipo" ,"link", "descricao")
    search_fields = ("nome",)

admin.site.register(Tecnologia,TecnologiaAdmin)