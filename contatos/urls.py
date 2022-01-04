from django.urls import path
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_contato>', views.view, name='visualizar_contato'),
    path('buscar/', views.search, name='buscar'),
    path('login/', RedirectView.as_view(url='accounts:login'), name='login')
]
