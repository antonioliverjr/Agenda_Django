#from django.db import models
from django.contrib.auth.models import User
from django import forms


class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(attrs={'required': True})
        }


class FormUserCadastro(FormUser):
    check_password = forms.CharField(max_length='128', widget=forms.PasswordInput(), label='Conferir Senha')

    class Meta(FormUser.Meta):
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'check_password',)

    def clean(self):
        verificar = super().clean()
        senha = verificar.get('password')
        senha2 = verificar.get('check_password')
        email = verificar.get('email')
        username = verificar.get('username')

        if User.objects.filter(username=username).exists():
            msg = 'Usuário já cadastrado, informe outro nome de usuário.'
            self.add_error('username', msg)

        if User.objects.filter(email=email).exists():
            msg = 'Este e-mail já está cadastrado em nosso sistema.'
            self.add_error('email', msg)

        if senha != senha2:
            msg = 'Digite Senha e Conferir Senha com o mesmo valor.'
            self.add_error('password', msg)
            self.add_error('check_password', msg)
