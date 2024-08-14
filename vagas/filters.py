import django_filters
from .models import Vaga

class VagaFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    local = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Vaga
        fields = ['titulo', 'local']