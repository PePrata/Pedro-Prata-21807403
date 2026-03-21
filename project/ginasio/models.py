from django.db import models

# Create your models here.

class Instrutor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aula(models.Model):
    nome = models.CharField(max_length=100)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    aulas = models.ManyToManyField(Aula, through='InscricaoAula')

    def __str__(self):
        return self.nome  # Never reference self.aulas here

class InscricaoAula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.aluno} → {self.aula}'