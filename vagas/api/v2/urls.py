from rest_framework.routers import DefaultRouter

from .views import CandidaturaViewSet, EmpresaViewSet, VagaViewSet

router = DefaultRouter()
router.register(r"vagas", VagaViewSet)
router.register(r"empresas", EmpresaViewSet)
router.register(r"candidaturas", CandidaturaViewSet)
urlpatterns = router.urls
