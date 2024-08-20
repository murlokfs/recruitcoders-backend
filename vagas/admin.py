from django.contrib import admin
from .models import Vaga, Empresa, Local, Candidatura, Curriculo

@admin.register(Vaga)
class Vaga(admin.ModelAdmin):
    list_display = ["pk", "titulo", "empresa", "local", "criado_em", "atualizado_em", "valido_ate"]

@admin.register(Empresa)
class Empresa(admin.ModelAdmin):
    list_display = ["nome", "email"]

@admin.register(Curriculo)
class Curriculo(admin.ModelAdmin):
    pass

@admin.register(Candidatura)
class Etapa(admin.ModelAdmin):
    pass

@admin.register(Local)
class Local(admin.ModelAdmin):
    pass


# Register your models here.
