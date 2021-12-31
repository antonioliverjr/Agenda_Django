from django.shortcuts import render, get_object_or_404, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Contato
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    contatos = Contato.objects.order_by('-id').filter(ativo=True)

    paginator = Paginator(contatos, 1)
    pag = request.GET.get('pag')

    contatos = paginator.get_page(pag)

    return render(
        request,
        'contatos/index.html',
        {'contatos': contatos}
    )


def view(request, id_contato):
    contato = get_object_or_404(Contato, id=id_contato)

    if not contato.ativo:
        raise Http404("Contato solicitado não está ativo, contato o administrador!")

    return render(
        request,
        'contatos/view.html',
        {'contato': contato}
    )

def search(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')

    if not termo or termo is None:
        return HttpResponseRedirect('/')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        ativo=True
    )

    paginator = Paginator(contatos, 1)
    pag = request.GET.get('pag')

    contatos = paginator.get_page(pag)

    return render(
        request,
        'contatos/search.html',
        {'contatos': contatos, 'termo': termo}
    )
