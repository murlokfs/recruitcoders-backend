from django.contrib import admin
from .models import Vaga, Empresa, Stack, Local

@admin.register(Vaga)
class Vaga(admin.ModelAdmin):
    list_display = ["pk", "titulo", "local", "criado_em", "atualizado_em", "valido_ate"]

@admin.register(Empresa)
class Empresa(admin.ModelAdmin):
    list_display = ["nome", "email"]

@admin.register(Local)
class Local(admin.ModelAdmin):
    pass

@admin.register(Stack)
class Stack(admin.ModelAdmin):
    pass

# Register your models here.
