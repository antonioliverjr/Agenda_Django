from django.shortcuts import render


def cad_endereco(request, id_contato):
    return render(request, 'contatos/index.html')
