import django_filters
from .models import Vaga, Empresa

class VagaFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    local = django_filters.CharFilter(field_name='local__nome', lookup_expr='icontains')
    experiencia = django_filters.MultipleChoiceFilter(choices=Vaga.NIVEIS)
    contrato = django_filters.MultipleChoiceFilter(choices=Vaga.CONTRATOS)
    stack = django_filters.MultipleChoiceFilter(choices=Vaga.STACKS)

    class Meta:
        model = Vaga
        fields = ['titulo', 'local', 'experiencia', 'contrato', 'stack']