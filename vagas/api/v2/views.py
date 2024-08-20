from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from vagas.models import Vaga, Empresa
from vagas.serializers import VagaSerializer, EmpresaSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
# ============ API V2 ============

class VagaViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    queryset = Vaga.objects.all().order_by("atualizado_em")
    serializer_class = VagaSerializer

class EmpresaViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer