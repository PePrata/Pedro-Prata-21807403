from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'
    
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso,through='Inscricao')

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.aluno}: {self.curso}'