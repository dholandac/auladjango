from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','criada_em','concluida')
admin.site.register(Tarefa, TarefaAdmin)