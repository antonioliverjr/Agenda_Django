from django.shortcuts import render, HttpResponseRedirect
# get_object_or_404, Http404 (Substuidos pelo sistema de mensagem)
from django.core.paginator import Paginator
from .models import Contato
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    contatos = Contato.objects.order_by('-id').filter(ativo=True)

    paginator = Paginator(contatos, 25)
    pag = request.GET.get('pag')

    contatos = paginator.get_page(pag)

    return render(
        request,
        'contatos/index.html',
        {'contatos': contatos}
    )


def view(request, id_contato):
    try:
        contato = Contato.objects.get(id=id_contato)
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Contato não existe!")
        return HttpResponseRedirect('/')

    if not contato.ativo:
        messages.add_message(request, messages.WARNING, "Contato solicitado não está ativo, contato o administrador!")
        return HttpResponseRedirect('/')

    return render(
        request,
        'contatos/view.html',
        {'contato': contato}
    )


def search(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')

    if not termo or termo is None:
        messages.add_message(request, messages.INFO, 'Para realizar pesquisa digite um termo.')
        return HttpResponseRedirect('/')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        ativo=True
    )

    paginator = Paginator(contatos, 25)
    pag = request.GET.get('pag')

    contatos = paginator.get_page(pag)

    return render(
        request,
        'contatos/search.html',
        {'contatos': contatos, 'termo': termo}
    )
