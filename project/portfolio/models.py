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
    

class Formacao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    link = models.CharField(blank=True)
    data_conclusao = models.DateField()

    tecnologias = models.ManyToManyField(Tecnologia, related_name="formacoes", blank=True)

    def __str__(self):
        return self.nome
    

class AreaTematica(models.Model):
    nome = models.CharField(max_length=255, unique=True)
 
    def __str__(self):
        return f'{self.nome}'   


class TFC(models.Model):
    GRAU_CHOICES = [
        ("licenciatura", "Licenciatura"),
        ("mestrado", "Mestrado"),
        ("doutoramento", "Doutoramento"),
    ]
 
    DESTAQUE_CHOICES = [
        (0, "Normal"),
        (1, "Interessante"),
        (2, "Muito Interessante"),
        (3, "Destaque"),
    ]
 
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name="tfcs")
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    email_autor = models.EmailField(blank=True)
    supervisor = models.CharField(max_length=255)
    grau = models.CharField(max_length=50, choices=GRAU_CHOICES, default="mestrado")
    ano = models.PositiveSmallIntegerField(null=True, blank=True)
    resumo = models.TextField(blank=True)
    keywords = models.CharField(max_length=500, blank=True)
    link = models.URLField(blank=True)
    download = models.URLField(blank=True)
    destaque = models.PositiveSmallIntegerField(choices=DESTAQUE_CHOICES, default=0)
    tecnologias = models.ManyToManyField(Tecnologia, related_name="tfcs", blank=True)
    areas = models.ManyToManyField(AreaTematica, related_name="tfcs", blank=True)
 
    def __str__(self):
        return self.titulo