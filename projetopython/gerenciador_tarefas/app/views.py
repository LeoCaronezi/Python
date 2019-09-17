from django.shortcuts import render
from .forms import  Tarefaform
# Create your views here.
def listar_tarefas(request):
    return  render(request, 'gerenciador_tarefas/listar_tarefas.html')

def cadastra_tarefa (request):
    form_tarefa = Tarefaform()
    return render(request, 'gerenciador_tarefas/form_tarefas.html', {"form_tarefa " : form_tarefa})