from django.contrib.auth.models import User
from django.db import models


class Especie(models.Model):
    descricao = models.CharField(max_length=150)


class Raca(models.Model):
    descricao = models.CharField(max_length=150)
    especie = models.ForeignKey(Especie)


class Pet(models.Model):
    user = models.ForeignKey(User)
    nome = models.CharField(max_length=150)
    especie = models.ForeignKey(Especie)
    raca = models.ForeignKey(Raca)
    foto = models.ImageField(upload_to='img_pets')
    IDADE_CHOICES = (
        ('1 a 3 meses', '1 a 3 meses'),
        ('3 a 6 meses', '3 a 6 meses'),
        ('6 a 9 meses', '6 a 9 meses'),
        ('9 a 12 meses', '9 a 12 meses'),
        ('1 a 3 anos', '1 a 3 anos'),
        ('Acima de 3 anos', 'Acima de 3 anos'),
    )
    idade = models.CharField(max_length=20, choices=IDADE_CHOICES, default="1 a 3 meses")
    GENERO_CHOICES = (
        ('Fêmea', 'Fêmea'),
        ('Macho', 'Macho'),
    )
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES, default="Feminino")
    descricao = models.TextField(blank=True, null=True)
    uf_escolhas = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AM', 'AM'),
        ('AP', 'AP'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MG', 'MG'),
        ('MS', 'MS'),
        ('MT', 'MT'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('PR', 'PR'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('RS', 'RS'),
        ('SC', 'SC'),
        ('SE', 'SE'),
        ('SP', 'SP'),
        ('TO', 'TO')
    )
    uf = models.CharField(max_length=20, choices=uf_escolhas, default='RO')
    cidade = models.CharField(max_length=150)
    contato = models.CharField(max_length=255, blank=True, null=True)

class UserProfile(models.Model):
    usuario = models.OneToOneField(User, unique=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True, blank=True)
    uf_escolhas = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AM', 'AM'),
        ('AP', 'AP'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MG', 'MG'),
        ('MS', 'MS'),
        ('MT', 'MT'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('PR', 'PR'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('RS', 'RS'),
        ('SC', 'SC'),
        ('SE', 'SE'),
        ('SP', 'SP'),
        ('TO', 'TO')
    )
    estado = models.CharField(max_length=20, choices=uf_escolhas, default='RO')