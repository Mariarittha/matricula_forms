
from django.contrib import admin
from django.urls import path
from aluno.views import cadastro_aluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('matricula/', cadastro_aluno, name='matricula')
]
