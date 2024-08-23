from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from vagas.views import Index, VagaListView, VagaDetailView, CandidaturaListView, CurriculoCreateView, CurriculoUpdateView, CandidaturaCreateView, CandidaturaDeleteView, DashboardListView, DashboardCreateView, DashboardUpdateView, DashboardDeleteView, DashboardCandidaturasListView
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('vagas', VagaListView.as_view(), name="vaga-list-page"),
    path('vagas/<int:pk>', VagaDetailView.as_view(), name="vaga-detail-page"),
    path('vagas/<int:vaga_id>/candidatar/', CandidaturaCreateView.as_view(), name='candidatura-confirm-page'),

    path('candidaturas', CandidaturaListView.as_view(), name="candidaturas"),
    path('candidatura/<int:pk>/deletar', CandidaturaDeleteView.as_view(), name='candidatura-delete-page'),

    path('curriculo', CurriculoCreateView.as_view(), name="curriculo"),
    path('curriculo/<int:pk>/editar', CurriculoUpdateView.as_view(), name="curriculo-update"),

    path('dashboard/', DashboardListView.as_view(), name="dashboard"),
    path('dashboard/vaga/<int:pk>', DashboardCandidaturasListView.as_view(), name="dashboard-vaga-view"),
    path('dashboard/vaga/criar', DashboardCreateView.as_view(), name="dashboard-vaga-criar"),
    path('dashboard/vaga/<int:pk>/editar', DashboardUpdateView.as_view(), name="dashboard-vaga-editar"),
    path('dashboard/vaga/<int:pk>/deletar', DashboardDeleteView.as_view(), name="dashboard-vaga-deletar"),

    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    
    path('api/', include('vagas.api.v1.urls')),
    path('api/v2/', include('vagas.api.v2.urls')),

    path("__debug__/", include("debug_toolbar.urls")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)