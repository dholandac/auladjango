from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TarefaForm
from .models import Tarefa

def home(request):
    lista = Tarefa.objects.select_related('usuario', 'usuario__perfil').prefetch_related('etiquetas').all()
    for tarefa in lista:
        tarefa.etiquetas_lista = list(tarefa.etiquetas.all())
    
    if request.method == "GET":
        return render(request, 'tarefas/home.html', {'tarefas' : lista})

def add(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TarefaForm()

    return render(request, 'tarefas/adicionar.html', {'form' : form})

def tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa' : tarefa})

def remove(request):
    return HttpResponse("Removendo uma tarefa do sistema...")

def edit(request):
    return HttpResponse("Editando uma tarefa do sistema...")

def search(request):
    return HttpResponse("Buscando uma tarefa do sistema...")
