from rest_framework import serializers

from .models import Candidatura, Empresa, Vaga


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = [
            "titulo",
            "empresa",
            "salario",
            "descricao",
            "local",
            "experiencia",
            "contrato",
            "valido_ate",
            "criado_em",
            "atualizado_em",
            "qntd_etapas",
            "is_ativo",
        ]


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ["nome", "imagem", "email", "colaboradores", "tipo"]


class CandidaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatura
        fields = ["vaga", "candidato", "etapa", "is_ativa"]
