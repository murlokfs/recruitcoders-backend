from typing import Iterable

from django.contrib.auth.models import User
from django.db import models


class Curriculo(models.Model):
    FORMACOES = (
        ("ensino_fi", "Ensino Fundamental Incompleto"),
        ("ensino_fc", "Ensino Fundamental Completo"),
        ("ensino_mi", "Ensino Médio Incompleto"),
        ("ensino_mc", "Ensino Médio Completo"),
        ("ensino_mti", "Ensino Médio Técnico Incompleto"),
        ("ensino_mtc", "Ensino Médio Técnico Completo"),
        ("ensino_si", "Ensino Superior Incompleto"),
        ("ensino_sc", "Ensino Superior Completo"),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=50, blank=True)
    sobre_mim = models.TextField(blank=True)
    formacao = models.CharField(max_length=22, choices=FORMACOES, blank=True)
    habilidades = models.TextField(blank=True)
    atualizado_em = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return self.usuario.username


class Empresa(models.Model):
    TIPOEMPRESA = (
        ("startup", "StartUp"),
        ("pequenamedia", "Pequena/Média Empresa"),
        ("grande", "Grande Empresa"),
    )

    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="empresas", blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    tipo = models.CharField(
        max_length=20, choices=TIPOEMPRESA, default=TIPOEMPRESA[0:0]
    )

    def __str__(self):
        return self.nome

    def get_tipo_display(self):
        return dict(self.TIPOEMPRESA).get(self.tipo, self.tipo)


class Local(models.Model):
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.cidade} - {self.estado}"


class Vaga(models.Model):
    NIVEIS = (
        ("junior", "Júnior"),
        ("pleno", "Pleno"),
        ("senior", "Sênior"),
    )

    CONTRATOS = (("clt", "CLT"), ("pj", "PJ"), ("estagio", "Estágio"))

    STACKS = (
        ("python", "Python"),
        ("javascript", "JavaScript"),
        ("java", "Java"),
        ("csharp", "C#"),
        ("cplus", "C++"),
    )

    titulo = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()

    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=True)
    experiencia = models.CharField(
        max_length=6, choices=NIVEIS, default=NIVEIS[0:0]
    )
    stack = models.CharField(
        max_length=10, choices=STACKS, default=STACKS[0:0]
    )
    contrato = models.CharField(
        max_length=7, choices=CONTRATOS, default=CONTRATOS[0:0]
    )

    valido_ate = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)

    qntd_etapas = models.IntegerField()
    is_ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Candidatura(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    candidato = models.ForeignKey(User, on_delete=models.CASCADE)
    etapa = models.IntegerField()
    is_ativa = models.BooleanField()

    def __str__(self):
        return (
            f"{self.vaga}: {self.candidato} -  Etapa:"
            f" {self.etapa}/{self.vaga.qntd_etapas}"
        )
