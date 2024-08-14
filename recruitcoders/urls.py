from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from vagas.views import Index, VagaListView

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('vagas', VagaListView.as_view(), name="vagas"),

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    path('api/', include('vagas.api.v1.urls')),
    path('api/v2', include('vagas.api.v2.urls')),

    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)