from django.urls import path, include
from .views import (
    VagaListCreateView,
    VagaRetrieveUpdateDestroyView,
    EmpresaListCreateView,
    EmpresaRetrieveUpdateDestroyView,
    CandidaturaListCreateView,
    CandidaturaRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("vagas/", VagaListCreateView.as_view(), name="vaga-list-create"),
    path(
        "vagas/<int:pk>/", VagaRetrieveUpdateDestroyView.as_view(), name="vaga-detail"
    ),
    path("empresas/", EmpresaListCreateView.as_view(), name="empresa-list-create"),
    path(
        "empresas/<int:pk>/",
        EmpresaRetrieveUpdateDestroyView.as_view(),
        name="empresa-detail",
    ),
    path(
        "candidaturas/", CandidaturaListCreateView.as_view(), name="empresa-list-create"
    ),
    path(
        "candidaturas/<int:pk>/",
        CandidaturaRetrieveUpdateDestroyView.as_view(),
        name="empresa-detail",
    ),
]
