from django.db import models

# Create your models here.

#Curso: id do curso, nome, imagem;

#Professor: id do professor, nome, email;

#Aluno: id do aluno, número, nome.

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    num = models.IntegerField()
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='ficha7_escola/fotos', null=True, blank=True)
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE,related_name="cursos")
    alunos = models.ManyToManyField(Aluno,related_name="cursos")

    def __str__(self):
        return self.nome
    
    #python manage.py makemigrations
