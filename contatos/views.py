from django.shortcuts import render, HttpResponseRedirect
# get_object_or_404, Http404 (Substuidos pelo sistema de mensagem)
from django.core.paginator import Paginator
from .models import Contato, FormContato
from enderecos.models import Endereco
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
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


@login_required(redirect_field_name='login')
def view(request, id_contato):
    try:
        contato = Contato.objects.get(id=id_contato)
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Contato não existe!")
        return HttpResponseRedirect('/')

    if not contato.ativo:
        messages.add_message(request, messages.WARNING, "Contato solicitado não está ativo, contato o administrador!")
        return HttpResponseRedirect('/')

    try:
        endereco = Endereco.objects.get(nome_contato=id_contato)
    except Exception as e:
        messages.info(request, "Contato não possui endereço!")
        return render(request, 'contatos/view.html', {'contato': contato})

    return render(request, 'contatos/view.html', {'contato': contato, 'endereco': endereco})


@login_required(redirect_field_name='login')
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

@login_required(redirect_field_name='login')
def inserir_contato(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'contatos/form.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        form = FormContato(request.POST)
        messages.error(request, 'Formulário contém dados invalidos!')
        return render(request, 'contatos/form.html', {'form': form})
    else:
        form.save()
        messages.success(request, "Contato cadastrado com sucesso!")
        return HttpResponseRedirect('/')

