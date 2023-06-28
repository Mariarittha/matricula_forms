from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):

    class Meta: 
        model=Aluno
        fields='__all__'
        widgets={
            "nome" : forms.TextInput(attrs={'class ': 'form-control', 'placeholder' : ' Nome do aluno'}),
            "email" : forms.EmailInput(attrs={'class ': 'form-control', 'placeholder' : 'Informe seu emial'}),
            "enderco" : forms.TextInput(attrs={'class ': 'form-control'}),
            "cidade" : forms.Select(attrs={'class ': 'form-control'}),
            "curso" : forms.Select(attrs={'class ': 'form-control'}),
        }