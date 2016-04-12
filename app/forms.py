# -*- coding: utf-8 -*-
from django import forms 
from app.models import *

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'ano_publicacao', 'autor']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome',]