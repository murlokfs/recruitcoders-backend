from django.contrib import admin
from .models import Vaga, Empresa, Tag

@admin.register(Vaga)
class Vaga(admin.ModelAdmin):
    list_display = ["pk", "titulo", "local", "criado_em", "atualizado_em", "valido_ate"]

@admin.register(Empresa)
class Empresa(admin.ModelAdmin):
    list_display = ["nome", "email"]

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass

# Register your models here.
