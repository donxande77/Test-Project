from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tarefas_home(request):
    context = {
        'nome': 'Alexandre'
       }
    return render(request, 'pagestarefas/home.html', context)

def tarefas_adicionar(request):
    return render(request, 'pagestarefas/adicionar.html')

def tarefas_editar(request):
    return render(request, 'pagestarefas/editar.html')

def tarefas_excluir(request):
    return render(request, 'pagestarefas/excluir.html')