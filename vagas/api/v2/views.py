from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from vagas.models import Vaga, Empresa
from vagas.serializers import VagaSerializer, EmpresaSerializer

# ============ API V2 ============

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all().order_by("atualizado_em")
    serializer_class = VagaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
