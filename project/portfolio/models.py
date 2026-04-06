from django.db import models

# Create your models here.
class Licenciatura(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

class Tecnologia(models.Model):
    nome = models.CharField(max_length=255)
    logotipo = models.ImageField(upload_to='portfolio/fotos', null=True, blank=True)
    link = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

class Docente(models.Model):
    nome = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255,blank=True)