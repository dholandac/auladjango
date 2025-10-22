from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    frase = "Hello World!"
    if request.method == "GET":
        return render(request, 'tarefas/home.html')

def add(request):
    if request.method == "GET":
        return render(request, 'tarefas/adicionar.html')

def remove(request):
    return HttpResponse("Removendo uma tarefa do sistema...")

def edit(request):
    return HttpResponse("Editando uma tarefa do sistema...")

def search(request):
    return HttpResponse("Buscando uma tarefa do sistema...")
