from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tarefas_home(request):
    return HttpResponse("<h1>Aqui estão suas tarefas!</h1>")

def tarefas_adicionar(request):
    return HttpResponse("<h1>Adicionar nova tarefa</h1>")