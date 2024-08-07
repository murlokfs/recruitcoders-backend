from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    titulo = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    salario = models.PositiveIntegerField()
    descricao = models.TextField()
    local = models.CharField(max_length=30)

    valido_ate = models.DateField()
    criado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)

    is_ativo = models.BooleanField(default=True)
    candidaturas = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.titulo

# Create your models here.
