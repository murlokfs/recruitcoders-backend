from .views import VagaViewSet, EmpresaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"vagas", VagaViewSet)
router.register(r"empresas", EmpresaViewSet)
urlpatterns = router.urls