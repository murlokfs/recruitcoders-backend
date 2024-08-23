import django_filters
from .models import Vaga, Candidatura


class VagaFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr="icontains")
    local = django_filters.CharFilter(
        field_name="local__cidade", lookup_expr="icontains"
    )
    experiencia = django_filters.MultipleChoiceFilter(choices=Vaga.NIVEIS)
    contrato = django_filters.MultipleChoiceFilter(choices=Vaga.CONTRATOS)
    stack = django_filters.MultipleChoiceFilter(choices=Vaga.STACKS)

    class Meta:
        model = Vaga
        fields = ["titulo", "local", "experiencia", "contrato", "stack"]


class CandidaturaFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(
        field_name="vaga__titulo", lookup_expr="icontains"
    )
    local = django_filters.CharFilter(
        field_name="vaga__local__cidade", lookup_expr="icontains"
    )
    experiencia = django_filters.MultipleChoiceFilter(
        field_name="vaga__experiencia", choices=Vaga.NIVEIS
    )
    contrato = django_filters.MultipleChoiceFilter(
        field_name="vaga__contrato", choices=Vaga.CONTRATOS
    )
    stack = django_filters.MultipleChoiceFilter(
        field_name="vaga__stack", choices=Vaga.STACKS
    )

    class Meta:
        model = Candidatura
        fields = ["titulo", "local", "experiencia", "contrato", "stack"]
