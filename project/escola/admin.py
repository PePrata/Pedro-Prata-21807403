from django.contrib import admin

from .models import Professor, Curso, Aluno, Inscricao
# Register your models here.

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'lista_cursos')
    search_fields = ('nome',)

    def lista_cursos(self, obj):
        return ", ".join(c.nome for c in obj.curso_set.all())

admin.site.register(Professor, ProfessorAdmin)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'professor')
    list_filter = ('professor',)
    search_fields = ('nome',)

admin.site.register(Curso, CursoAdmin)


class InscricaoInline(admin.TabularInline):
    model = Inscricao
    extra = 1


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'lista_cursos')
    search_fields = ('nome',)
    inlines = [InscricaoInline]  # Embed the enrollment form inside the student page

    def lista_cursos(self, obj):
        print(f"DEBUG: {obj.nome} has inscricoes: {obj.inscricao_set.all()}")
        inscricoes = obj.inscricao_set.all()
        if not inscricoes.exists():
            return "Sem cursos"
        return ", ".join(i.curso.nome for i in inscricoes)

admin.site.register(Aluno, AlunoAdmin)


class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso')
    list_filter = ('curso',)
    search_fields = ('aluno__nome', 'curso__nome')

admin.site.register(Inscricao, InscricaoAdmin)