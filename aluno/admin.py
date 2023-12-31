from django.contrib import admin
from .models import Aluno, Cidade, Curso

@admin.register(Aluno)
class AlunoAdmin (admin.ModelAdmin):
    list_display = ('nome', 'email', 'endereco',  'cidade', 'curso',)

@admin.register(Curso)
class CursoAdmin (admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Cidade)
class CidadeAdmin (admin.ModelAdmin):
    list_display = ('nome', 'sigla_estado',)



