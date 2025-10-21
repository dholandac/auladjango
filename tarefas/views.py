from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    frase = "Hello World!"
    return HttpResponse(frase)

def add(request):
    return HttpResponse("Adicionando uma nova tarefa ao sistema...")

def remove(request):
    return HttpResponse("Removendo uma tarefa do sistema...")

def edit(request):
    return HttpResponse("Editando uma tarefa do sistema...")

def search(request):
    return HttpResponse("Buscando uma tarefa do sistema...")