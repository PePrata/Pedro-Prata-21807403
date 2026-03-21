from django.contrib import admin

from .models import Utilizador, Ingrediente, Receita

# Register your models here.

class UtilizadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'lista_receitas', 'lista_favoritos')
    search_fields = ('nome',)

    def lista_receitas(self, obj):
        receitas = obj.receita_set.all()
        if not receitas.exists():
            return "Sem receitas"
        return ", ".join(r.titulo for r in receitas)
    lista_receitas.short_description = 'Receitas Criadas'

    def lista_favoritos(self, obj):
        favoritos = obj.receitas_favoritas.all()
        if not favoritos.exists():
            return "Sem favoritos"
        return ", ".join(r.titulo for r in favoritos)
    lista_favoritos.short_description = 'Receitas Favoritas'

admin.site.register(Utilizador, UtilizadorAdmin)

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Ingrediente, IngredienteAdmin)

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'criador', 'lista_ingredientes', 'lista_favoritos')
    list_filter = ('criador',)
    search_fields = ('titulo', 'criador__nome')
    filter_horizontal = ('ingredientes', 'favoritos')  # nicer UI for ManyToMany

    def lista_ingredientes(self, obj):
        ingredientes = obj.ingredientes.all()
        if not ingredientes.exists():
            return "Sem ingredientes"
        return ", ".join(i.nome for i in ingredientes)
    lista_ingredientes.short_description = 'Ingredientes'

    def lista_favoritos(self, obj):
        favoritos = obj.favoritos.all()
        if not favoritos.exists():
            return "Sem favoritos"
        return ", ".join(u.nome for u in favoritos)
    lista_favoritos.short_description = 'Favoritos'

admin.site.register(Receita, ReceitaAdmin)