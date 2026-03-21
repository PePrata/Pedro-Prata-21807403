from django.contrib import admin

from .models import Instrutor, Aula, Aluno, InscricaoAula

# Register your models here.

class AulaInline(admin.TabularInline):
    model = Aula
    extra = 1

class InstrutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'lista_aulas')
    search_fields = ('nome',)
    inlines = [AulaInline]

    def lista_aulas(self, obj):
        aulas = obj.aula_set.all()
        if not aulas.exists():
            return "Sem aulas"
        return ", ".join(a.nome for a in aulas)

admin.site.register(Instrutor, InstrutorAdmin)

class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'instrutor')
    list_filter = ('instrutor',)
    search_fields = ('nome',)

admin.site.register(Aula, AulaAdmin)

class InscricaoAulaInline(admin.TabularInline):
    model = InscricaoAula
    extra = 1
    readonly_fields = ('data',)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'lista_aulas')
    search_fields = ('nome',)
    inlines = [InscricaoAulaInline]

    def lista_aulas(self, obj):
        inscricoes = obj.inscricaoaula_set.all()
        if not inscricoes.exists():
            return "Sem aulas"
        return ", ".join(i.aula.nome for i in inscricoes)

admin.site.register(Aluno, AlunoAdmin)

class InscricaoAulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'aula', 'data')
    list_filter = ('aula',)
    search_fields = ('aluno__nome', 'aula__nome')
    readonly_fields = ('data',)

admin.site.register(InscricaoAula, InscricaoAulaAdmin)