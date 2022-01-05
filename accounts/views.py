from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from .models import FormUserCadastro, FormUser


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario_email = request.POST.get('username')
    senha = request.POST.get('password')

    if usuario_email is None or senha is None:
        messages.error(request, "Informe usuário e senha!")
        return render(request, 'accounts/login.html')

    user = auth.authenticate(request, username=usuario_email, password=senha)

    if not user:
        messages.error(request, "Usuário não autenticado, verifique os dados informados.")
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        msg = f"Seja bem vindo {user.first_name} {user.last_name}!"
        messages.success(request, msg)
        return redirect('/')


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
    auth.logout(request)
    messages.warning(request, 'Logout Efetuado!')
    return redirect('/')
