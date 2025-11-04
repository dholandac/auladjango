from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .forms import TarefaForm
from .models import Tarefa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name="usuarios_normais")
            user.groups.add(group)

            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form' : form})

@login_required
@permission_required("tarefas.delete_tarefa")
def remove(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    
    if not request.user.has_perm("tarefas.can_view_all_tarefas"):
        if tarefa.usuario != request.user:
            return redirect('home')
    
    if request.method == "POST":
        tarefa.delete()
        return redirect('home')
    
    return render(request, 'tarefas/remover.html', {'tarefa': tarefa})

@login_required
@permission_required("tarefas.change_tarefa")
def edit(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    
    if not request.user.has_perm("tarefas.can_view_all_tarefas"):
        if tarefa.usuario != request.user:
            return redirect('home')
    
    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('individual', id=tarefa.id)
    else:
        form = TarefaForm(instance=tarefa)
    
    return render(request, 'tarefas/editar.html', {'form': form, 'tarefa': tarefa})

@login_required
def search(request):
    query = request.GET.get('q', '')
    tarefas = Tarefa.objects.select_related('usuario', 'usuario__perfil').prefetch_related('etiquetas').all()
    
    if request.user.has_perm("tarefas.can_view_all_tarefas"):
        tarefas = tarefas.all()
    else:
        tarefas = tarefas.filter(usuario=request.user)
    
    if query:
        tarefas = tarefas.filter(titulo__icontains=query) | tarefas.filter(descricao__icontains=query)
    
    for tarefa in tarefas:
        tarefa.etiquetas_lista = list(tarefa.etiquetas.all())
    
    return render(request, 'tarefas/buscar.html', {'tarefas': tarefas, 'query': query})
