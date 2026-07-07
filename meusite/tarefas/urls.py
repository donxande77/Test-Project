from django.urls import path
from . import view

urlpatterns = [
    path('', view.tarefas_home),
    path('adicionar/', view.tarefas_adicionar),
]