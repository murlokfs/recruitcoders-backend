from .views import VagaViewSet, EmpresaViewSet, CandidaturaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"vagas", VagaViewSet)
router.register(r"empresas", EmpresaViewSet)
router.register(r"candidaturas", CandidaturaViewSet)
urlpatterns = router.urls
