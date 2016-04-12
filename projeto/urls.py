
from app.models import *
from app.views import *
from app.forms import *
from vanilla import CreateView, DeleteView, ListView, UpdateView, TemplateView
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    #
    # CBV
    url(r'^cadastrarCBV/$', CadastrarCBV.as_view(tipoForm=AutorForm),
        name='cadastrar cbv'),
    url(r'^templateCBV/$', templateCBV.as_view()),
    #  
    # GenericViews
    url(r'^templateGV/$', templateGenerics.as_view()),
    url(r'^cadastrarGV/$', CadastrarGenerics.as_view(), name='cadastrar generics'),
    url(r'^listarGV/$', ListarGenerics.as_view(), name='listar generics'),
    url(r'^detalharGV/(?P<pk>\d+)/$', DetalharGenerics.as_view(),
        name='detalhar gv'),
    url(r'^editarGV/(?P<pk>\d+)/$', EditarGenerics.as_view(), name='editar generics'),
    url(r'^deletarGV/(?P<pk>\d+)/$', DeletarGenerics.as_view(), name='deletar generics'),
]