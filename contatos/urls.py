from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_contato>', views.view, name='visualizar_contato'),
    path('buscar/', views.search, name='buscar'),
    path('inserir/', views.inserir_contato, name='inserir'),
    path('endereco', RedirectView.as_view(url='agenda:enderecos'), name='endereco'),
    path('login/', RedirectView.as_view(url='accounts:login'), name='login'),
    path('admin/', RedirectView.as_view(url='agenda:painel'), name='painel')
]
