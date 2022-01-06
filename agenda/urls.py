"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contatos import views as v_contatos
from accounts import views as v_accounts
from enderecos import views as v_enderecos


urlpatterns = [
    path('', include([
        path('', v_contatos.index, name='index'),
        path('<int:id_contato>', v_contatos.view, name='visualizar_contato'),
        path('buscar/', v_contatos.search, name='buscar'),
        path('inserir/', v_contatos.inserir_contato, name='inserir')
    ])),
    path('accounts/', include([
        path('', v_accounts.login, name='index_account'),
        path('login/', v_accounts.login, name='login'),
        path('cadastro/', v_accounts.cadastro, name='cadastro'),
        path('logout/', v_accounts.logout, name='logout'),
    ])),
    path('enderecos/', include([
        path('<int:id_contato>', v_enderecos.get_endereco, name='endereco'),
        path('cadastrar/', v_enderecos.cad_endereco, name='cadastrar'),
    ])),
    path('admin/', admin.site.urls, name='admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
