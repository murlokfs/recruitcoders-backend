from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="empresas", blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    titulo = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=6,decimal_places=2)
    descricao = models.TextField()
    local = models.CharField(max_length=30)
    tags = models.ManyToManyField(Tag, verbose_name="tags", blank=True)

    valido_ate = models.DateField()
    criado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)

    is_ativo = models.BooleanField(default=True)
    candidaturas = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.titulo

