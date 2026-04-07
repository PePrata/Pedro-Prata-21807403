from django.db import models

# Create your models here.
class Licenciatura(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nome}'

class Tecnologia(models.Model):
    nome = models.CharField(max_length=255)
    logotipo = models.ImageField(upload_to='portfolio/fotos', null=True, blank=True)
    link = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nome}'

class Docente(models.Model):
    nome = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return f'{self.nome}'


class Cadeira(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name="cadeiras")
    nome = models.CharField(max_length=255)
    ano = models.IntegerField()
    descricao = models.TextField(blank=True)

    docentes = models.ManyToManyField(Docente, related_name="cadeiras")
    tecnologias = models.ManyToManyField(Tecnologia, related_name="cadeiras", blank=True)

    def __str__(self):
        return f'{self.nome}'


class Projeto(models.Model):
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE, related_name="projetos")
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    link = models.TextField(blank=True)

    tecnologias = models.ManyToManyField(Tecnologia, related_name="projetos", blank=True)

    def __str__(self):
        return self.nome