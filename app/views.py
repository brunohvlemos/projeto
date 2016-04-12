# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from app.models import *
from app.forms import *
from django.views.generic import View
from vanilla import CreateView, DeleteView, ListView, DetailView, UpdateView, TemplateView


class CadastrarCBV(View):

    tipoForm = None


    def get(self, request):
        form = self.tipoForm()
        return render(request, 'cadastro.html', locals())

    def post(self, request):
        form = self.tipoForm(request.POST)
        if form.is_valid():
            cadastro_object = form.save()
            form = self.tipoForm()
        return render(request, 'cadastro.html', locals())



class templateCBV(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class templateGenerics(TemplateView):
    



class CadastrarGenerics(CreateView):
    


class DetalharGenerics(DetailView):
    


class ListarGenerics(ListView):
    


class EditarGenerics(UpdateView):
    


class DeletarGenerics(DeleteView):
    