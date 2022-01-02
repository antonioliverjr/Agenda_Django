from django.shortcuts import render
from django.contrib import messages
from .models import FormUserCadastro, FormUser


def login(request):
    return render(request, 'accounts/login.html')


def cadastro(request):
    if request.method != 'POST':
        form = FormUserCadastro()
        print(form)
        return render(request, 'accounts/cadastro.html', {'form': form})

    form = FormUserCadastro(request.POST)
    if form.is_valid():
        user = FormUser.Meta.model.objects.create_user(
            username=request.POST.get('username'), email=request.POST.get('email'),
            password=request.POST.get('password'), first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'))
        user.save()
        messages.success(request, "Usuário cadastrado com sucesso!")

    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')
