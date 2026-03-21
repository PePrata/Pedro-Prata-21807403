from django.db import models

# Create your models here.

# Desporto
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="atletas")

    def __str__(self):
        return self.nome

class Desporto(models.Model):
    nome = models.CharField(max_length=100)
    atletas = models.ManyToManyField(Atleta, related_name='desportos')

    def __str__(self):
        return self.nome


# Biblioteca
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    ano_nascimento = models.IntegerField(default=None)
    nacionalidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField(default=None)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="livros")
    genero = models.CharField(max_length=100)
    editora = models.CharField(max_length=100, default=None)
    isbn = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.titulo

class Leitor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_admissao = models.DateField()

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="emprestimos")
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE, related_name="emprestimos")
    data_emprestimo = models.DateField(default=None)
    data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.leitor} requisitou {self.livro}"


# Campeonato
class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()

    def __str__(self):
        return self.nome

class Prova(models.Model):
    nome = models.CharField(max_length=100)
    campeonatos = models.ManyToManyField(Campeonato, related_name='provas')

    def __str__(self):
        return self.nome

class Nadador(models.Model):
    nome = models.CharField(max_length=100)
    campeonatos = models.ManyToManyField(Campeonato, related_name='nadadores')

    def __str__(self):
        return self.nome

class Resultado(models.Model):
    nadador = models.ForeignKey(Nadador, on_delete=models.CASCADE, related_name='resultados')
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE, related_name='resultados')
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE, related_name='resultados')
    classificacao = models.IntegerField()

    class Meta:
        unique_together = ('nadador', 'campeonato', 'prova')

    def __str__(self):
        return f"{self.nadador.nome} - {self.prova.nome} ({self.campeonato.nome}): {self.classificacao}º"