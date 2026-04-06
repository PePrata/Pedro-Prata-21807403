from django.db import models

# Create your models here.
class Licenciatura(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)