from django.db import models

# Create your models here.

class Utilizador(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    titulo = models.CharField(max_length=100)
    criador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)
    favoritos = models.ManyToManyField(Utilizador, related_name='receitas_favoritas')

    def __str__(self):
        return self.titulo