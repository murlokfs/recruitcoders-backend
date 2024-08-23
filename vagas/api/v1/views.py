from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import Group
from vagas.models import Vaga, Empresa, Candidatura
from vagas.serializers import VagaSerializer, EmpresaSerializer, CandidaturaSerializer
from rest_framework.permissions import IsAdminUser

# ============ API V1 ============

class VagaListCreateView(generics.ListCreateAPIView):
    queryset = Vaga.objects.all().order_by("atualizado_em")
    serializer_class = VagaSerializer
    permission_classes = [IsAdminUser]

class VagaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    permission_classes = [IsAdminUser]

class EmpresaListCreateView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAdminUser]

class EmpresaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAdminUser]

class CandidaturaListCreateView(generics.ListCreateAPIView):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer
    permission_classes = [IsAdminUser]

class CandidaturaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer
    permission_classes = [IsAdminUser]
