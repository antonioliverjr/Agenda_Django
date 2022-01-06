from django.db import models
from django import forms
from contatos.models import Contato

class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255)
    localidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    nome_contato = models.ForeignKey(Contato, on_delete=models.DO_NOTHING)

    def __str__(self):
        self.endereco_contato = f'{self.nome_contato}-{self.cep}'
        return self.endereco_contato

class FormEndereco(forms.ModelForm):
    class Meta:
        model = Endereco
        exclude = ()
