from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from vagas.views import Index

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/v2/', include('vagas.api.v2.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
