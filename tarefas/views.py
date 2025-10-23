from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TarefaForm

def home(request):
    if request.method == "GET":
        return render(request, 'tarefas/home.html')

def add(request):
    form = TarefaForm()

    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'tarefas/adicionar.html', {'form' : form})

def remove(request):
    return HttpResponse("Removendo uma tarefa do sistema...")

def edit(request):
    return HttpResponse("Editando uma tarefa do sistema...")

def search(request):
    return HttpResponse("Buscando uma tarefa do sistema...")
