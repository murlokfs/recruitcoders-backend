from django.urls import include, path

from .views import (CandidaturaListCreateView,
                    CandidaturaRetrieveUpdateDestroyView,
                    EmpresaListCreateView, EmpresaRetrieveUpdateDestroyView,
                    VagaListCreateView, VagaRetrieveUpdateDestroyView)

urlpatterns = [
    path("vagas/", VagaListCreateView.as_view(), name="vaga-list-create"),
    path(
        "vagas/<int:pk>/",
        VagaRetrieveUpdateDestroyView.as_view(),
        name="vaga-detail",
    ),
    path(
        "empresas/",
        EmpresaListCreateView.as_view(),
        name="empresa-list-create",
    ),
    path(
        "empresas/<int:pk>/",
        EmpresaRetrieveUpdateDestroyView.as_view(),
        name="empresa-detail",
    ),
    path(
        "candidaturas/",
        CandidaturaListCreateView.as_view(),
        name="empresa-list-create",
    ),
    path(
        "candidaturas/<int:pk>/",
        CandidaturaRetrieveUpdateDestroyView.as_view(),
        name="empresa-detail",
    ),
]
