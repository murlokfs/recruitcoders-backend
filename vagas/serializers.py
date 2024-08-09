from .models import Vaga, Empresa
from rest_framework import serializers

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = [
            "titulo",
            "empresa",
            "salario",
            "descricao",
            "local",
            "valido_ate",
            "criado_em",
            "atualizado_em",
            "is_ativo",
            "candidaturas",
        ]

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            "nome",
            "email",
        ]