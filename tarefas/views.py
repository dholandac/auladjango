from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .forms import TarefaForm
from .models import Tarefa
from django.contrib.auth.forms import UserCreationForm

@login_required
def home(request):
    lista = Tarefa.objects.select_related('usuario', 'usuario__perfil').prefetch_related('etiquetas').all()

    if request.user.has_perm("tarefas.can_view_all_tarefas"):
        lista = lista.all()
    else:
        lista = lista.filter(usuario=request.user)

    for tarefa in lista:
        tarefa.etiquetas_lista = list(tarefa.etiquetas.all())
    
    if request.method == "GET":
        return render(request, 'tarefas/home.html', {'tarefas' : lista})

@permission_required("tarefas.add_tarefa")
def add(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            form.save()
            form.save_m2m()
            return redirect('home')

    form = TarefaForm()
    return render(request, 'tarefas/adicionar.html', {'form' : form})

def tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa' : tarefa})

def register(request):
    if request.method == 'POST':
        pass
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form' : form})

def remove(request):
    return HttpResponse("Removendo uma tarefa do sistema...")

def edit(request):
    return HttpResponse("Editando uma tarefa do sistema...")

def search(request):
    return HttpResponse("Buscando uma tarefa do sistema...")
