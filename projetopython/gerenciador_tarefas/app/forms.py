from django import forms
from .models import Tarefa

class Tarefaform(forms.ModelForm):
     class Meta:
         mode = Tarefa
         fields ='__all__'