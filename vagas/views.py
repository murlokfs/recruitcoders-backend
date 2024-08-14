from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from .models import Vaga

class Index(TemplateView):
    template_name = "index.html"

class VagaListView(ListView):
    model = Vaga
    template_name = "vagas.html"
    context_object_name = "vagas"

    def get_queryset(self):
        return Vaga.objects.all().filter(is_ativo=True)

    
    