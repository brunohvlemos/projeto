# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
    	return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=64)
    ano_publicacao = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
