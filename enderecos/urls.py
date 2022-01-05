from django.urls import path
from . import views

urlpatterns = [
    path('<int:id_contato>', views.cad_endereco, name='endereco')
]