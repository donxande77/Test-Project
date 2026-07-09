from django.urls import path
from . import view

app_name = 'tarefas'
urlpatterns = [
    path('', view.tarefas_home, name='home'),
    path('adicionar/', view.tarefas_adicionar, name='adicionar'),
    path('editar/', view.tarefas_editar, name='editar'),
    path('excluir/', view.tarefas_excluir, name='excluir'),
]