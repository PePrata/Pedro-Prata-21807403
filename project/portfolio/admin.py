from django.contrib import admin

from .models import Licenciatura,Tecnologia,Docente,Cadeira,Projeto

# Register your models here.

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)

admin.site.register(Licenciatura, LicenciaturaAdmin)

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome","logotipo" ,"link", "descricao")
    search_fields = ("nome",)

admin.site.register(Tecnologia,TecnologiaAdmin)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome","linkedin")
    search_fields = ("nome",)

admin.site.register(Docente,DocenteAdmin)

class CadeiraAdmin(admin.ModelAdmin):
    list_display = ("nome","ano","descricao","listar_docentes","listar_tecnologias")
    search_fields = ("nome","ano",)

    def listar_docentes(self, obj):
        return ", ".join([d.nome for d in obj.docentes.all()])

    def listar_tecnologias(self, obj):
        return ", ".join([t.nome for t in obj.tecnologias.all()])

admin.site.register(Cadeira,CadeiraAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "cadeira", "link","listar_tecnologias", "descricao")
    list_filter = ("cadeira", "tecnologias")
    search_fields = ("nome", "descricao")

    def listar_tecnologias(self, obj):
        return ", ".join([t.nome for t in obj.tecnologias.all()])

admin.site.register(Projeto,ProjetoAdmin)