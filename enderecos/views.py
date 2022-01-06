from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from .models import FormEndereco
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def get_endereco(request, id_contato):
    if request.method != 'POST':
        form = FormEndereco()
        form.fields['nome_contato'].initial = [id_contato]
        print(form)
        return render(request, 'enderecos/form.html', {'form': form, 'id_contato': id_contato})


@login_required(redirect_field_name='login')
def cad_endereco(request):
    if request.method != 'POST':
        messages.error(request, "Para cadastro acesso o formulário.")
        return redirect('/')

    id_contato = request.POST.get('nome_contato')
    form = FormEndereco(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, "Endereço cadastrado com sucesso!")
        return redirect(f'/{id_contato}')

    messages.error(request, "Dados incompletos para cadastro...")
    return render(request, 'enderecos/form.html', {'form': form})
