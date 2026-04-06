from django.contrib import admin

from .models import Licenciatura

# Register your models here.

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)

admin.site.register(Licenciatura, LicenciaturaAdmin)