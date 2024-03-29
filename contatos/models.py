from django.db import models
from django import forms
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=13)
    email = models.CharField(max_length=255, blank=True, unique=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('ativo', 'data_criacao')

        widgets = {
            'email': forms.EmailInput(attrs={'required': True})
        }
