from django.db import models

#entidadaes tem muitos

class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    sigla_estado = models.CharField(max_length=2)

    
    def _str_(self):
        return self.nome

class Curso (models.Model):
    nome = models.CharField(max_length=150)

    def _str_(self):
        return self.nome

class Aluno (models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    endereco = models.CharField(max_length= 200)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def _str_(self):
        return self.nome


