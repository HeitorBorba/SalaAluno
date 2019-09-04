from django.db import models


# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome'
    )

    email = models.EmailField(
        max_length=255,
        verbose_name='E-mail',
        unique=True
    )
    idade = models.DateField(
        verbose_name='Idade'
    )