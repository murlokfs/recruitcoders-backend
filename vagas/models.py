from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    TIPOEMPRESA = (
        ("startup", "StartUp"),
        ("pequenamedia", "Pequena/Média Empresa"),
        ("grande", "Grande Empresa"),
    )

    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="empresas", blank=True)
    email = models.EmailField()
    tipo = models.CharField(max_length=20,choices=TIPOEMPRESA, default=TIPOEMPRESA[0:0])

    def __str__(self):
        return self.nome
    
    def get_tipo_display(self):
        return dict(self.TIPOEMPRESA).get(self.tipo, self.tipo)

class Local(models.Model):
    nome = models.CharField(max_length=30)
    def __str__(self):
        return self.nome

class Vaga(models.Model):
    NIVEIS = (
        ("junior", "Júnior"),
        ("pleno", "Pleno"),
        ("senior", "Sênior"),
    )

    CONTRATOS = (
        ("clt", "CLT"),
        ("pj", "PJ"),
        ("estagio", "Estágio")
    )

    STACKS = (
        ("python", "Python"),
        ("javascript", "JavaScript"),
        ("java", "Java"),
        ("csharp", "C#"),
        ("cplus", "C++"),
    )

    titulo = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=6,decimal_places=2)
    descricao = models.TextField()

    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=True)
    experiencia = models.CharField(max_length=6, choices=NIVEIS, default=NIVEIS[0:0])
    stack = models.CharField(max_length=10, choices=STACKS, default=STACKS[0:0])
    contrato = models.CharField(max_length=7, choices=CONTRATOS, default=CONTRATOS[0:0])

    valido_ate = models.DateField()
    criado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)

    is_ativo = models.BooleanField(default=True)
    candidaturas = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.titulo

