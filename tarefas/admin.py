from django.contrib import admin
from .models import Tarefa, Etiqueta, Perfil

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','criada_em','concluida')

admin.site.register(Tarefa, TarefaAdmin)

class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cor']

admin.site.register(Etiqueta, EtiquetaAdmin)

class PerfilAdmin (admin.ModelAdmin):
    list_display = ['bio', 'tema']

admin.site.register(Perfil, PerfilAdmin)