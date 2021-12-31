from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'sobrenome',
        'telefone',
        'email',
        'categoria',
        'ativo'
    )

    list_display_links = (
        'id',
        'nome',
        'sobrenome'
    )

    list_filter = (
        'nome',
        'sobrenome'
    )

    search_fields = (
        'nome',
        'telefone'
    )

    list_editable = (
        'telefone',
        'ativo'
    )

    list_per_page = 15


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)
