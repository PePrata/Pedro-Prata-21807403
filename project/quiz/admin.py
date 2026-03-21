from django.contrib import admin

from .models import Categoria, Atleta, Desporto, Autor, Livro, Leitor, Emprestimo, Campeonato, Prova, Nadador, Resultado

# Register your models here.

# Desporto
class AtletaInline(admin.TabularInline):
    model = Atleta
    extra = 1

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'lista_atletas')
    search_fields = ('nome',)
    inlines = [AtletaInline]

    def lista_atletas(self, obj):
        atletas = obj.atletas.all()
        if not atletas.exists():
            return "Sem atletas"
        return ", ".join(a.nome for a in atletas)
    lista_atletas.short_description = 'Atletas'

admin.site.register(Categoria, CategoriaAdmin)

class AtletaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'categoria', 'lista_desportos')
    list_filter = ('categoria',)
    search_fields = ('nome',)

    def lista_desportos(self, obj):
        desportos = obj.desportos.all()
        if not desportos.exists():
            return "Sem desportos"
        return ", ".join(d.nome for d in desportos)
    lista_desportos.short_description = 'Desportos'

admin.site.register(Atleta, AtletaAdmin)

class DesportoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'lista_atletas')
    search_fields = ('nome',)
    filter_horizontal = ('atletas',)

    def lista_atletas(self, obj):
        atletas = obj.atletas.all()
        if not atletas.exists():
            return "Sem atletas"
        return ", ".join(a.nome for a in atletas)
    lista_atletas.short_description = 'Atletas'

admin.site.register(Desporto, DesportoAdmin)

# Biblioteca
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nacionalidade', 'ano_nascimento', 'lista_livros')
    search_fields = ('nome', 'nacionalidade')
    inlines = [LivroInline]

    def lista_livros(self, obj):
        livros = obj.livros.all()
        if not livros.exists():
            return "Sem livros"
        return ", ".join(l.titulo for l in livros)
    lista_livros.short_description = 'Livros'

admin.site.register(Autor, AutorAdmin)

class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'genero', 'editora', 'ano_publicacao')
    list_filter = ('genero', 'autor')
    search_fields = ('titulo', 'autor__nome', 'isbn')

admin.site.register(Livro, LivroAdmin)

class EmprestimoInline(admin.TabularInline):
    model = Emprestimo
    extra = 1

class LeitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'data_admissao', 'lista_emprestimos')
    search_fields = ('nome', 'email')
    inlines = [EmprestimoInline]

    def lista_emprestimos(self, obj):
        emprestimos = obj.emprestimos.all()
        if not emprestimos.exists():
            return "Sem empréstimos"
        return ", ".join(e.livro.titulo for e in emprestimos)
    lista_emprestimos.short_description = 'Empréstimos'

admin.site.register(Leitor, LeitorAdmin)

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('id', 'leitor', 'livro', 'data_emprestimo', 'data_devolucao')
    list_filter = ('livro',)
    search_fields = ('leitor__nome', 'livro__titulo')

admin.site.register(Emprestimo, EmprestimoAdmin)

# Campeonato
class ResultadoInline(admin.TabularInline):
    model = Resultado
    extra = 1

class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data', 'lista_provas', 'lista_nadadores')
    search_fields = ('nome',)

    def lista_provas(self, obj):
        provas = obj.provas.all()
        if not provas.exists():
            return "Sem provas"
        return ", ".join(p.nome for p in provas)
    lista_provas.short_description = 'Provas'

    def lista_nadadores(self, obj):
        nadadores = obj.nadadores.all()
        if not nadadores.exists():
            return "Sem nadadores"
        return ", ".join(n.nome for n in nadadores)
    lista_nadadores.short_description = 'Nadadores'

admin.site.register(Campeonato, CampeonatoAdmin)

class ProvaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'lista_campeonatos')
    search_fields = ('nome',)
    filter_horizontal = ('campeonatos',)

    def lista_campeonatos(self, obj):
        campeonatos = obj.campeonatos.all()
        if not campeonatos.exists():
            return "Sem campeonatos"
        return ", ".join(c.nome for c in campeonatos)
    lista_campeonatos.short_description = 'Campeonatos'

admin.site.register(Prova, ProvaAdmin)

class NadadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'lista_campeonatos', 'lista_resultados')
    search_fields = ('nome',)
    filter_horizontal = ('campeonatos',)
    inlines = [ResultadoInline]

    def lista_campeonatos(self, obj):
        campeonatos = obj.campeonatos.all()
        if not campeonatos.exists():
            return "Sem campeonatos"
        return ", ".join(c.nome for c in campeonatos)
    lista_campeonatos.short_description = 'Campeonatos'

    def lista_resultados(self, obj):
        resultados = obj.resultados.all()
        if not resultados.exists():
            return "Sem resultados"
        return ", ".join(f'{r.prova.nome}: {r.classificacao}º' for r in resultados)
    lista_resultados.short_description = 'Resultados'

admin.site.register(Nadador, NadadorAdmin)

class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nadador', 'campeonato', 'prova', 'classificacao')
    list_filter = ('campeonato', 'prova')
    search_fields = ('nadador__nome', 'campeonato__nome', 'prova__nome')

admin.site.register(Resultado, ResultadoAdmin)