from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import Group
from vagas.models import Vaga, Empresa
from vagas.serializers import VagaSerializer, EmpresaSerializer
from rest_framework.permissions import IsAuthenticated

# ============ API V1 ============

class VagaListCreateView(generics.ListCreateAPIView):
    queryset = Vaga.objects.all().order_by("atualizado_em")
    serializer_class = VagaSerializer
    permission_classes = [IsAuthenticated]

class VagaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    permission_classes = [IsAuthenticated]

class EmpresaListCreateView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated]

class EmpresaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated]
