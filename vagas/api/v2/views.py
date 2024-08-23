from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from vagas.models import Vaga, Empresa, Candidatura
from vagas.serializers import VagaSerializer, EmpresaSerializer, CandidaturaSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAdminUser

# ============ API V2 ============


class VagaViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Vaga.objects.all().order_by("atualizado_em")
    serializer_class = VagaSerializer
    permission_classes = [IsAdminUser]


class EmpresaViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAdminUser]


class CandidaturaViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer
    permission_classes = [IsAdminUser]
