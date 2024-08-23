from django import forms
from .models import Curriculo, Vaga


class CurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = ["nome_completo", "sobre_mim", "formacao", "habilidades"]


class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = [
            "titulo",
            "salario",
            "descricao",
            "local",
            "experiencia",
            "stack",
            "contrato",
            "valido_ate",
            "qntd_etapas",
        ]
