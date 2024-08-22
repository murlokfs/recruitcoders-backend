from django import forms
from .models import Curriculo, Candidatura

class CurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = ['nome_completo', 'sobre_mim', 'formacao', 'habilidades']
