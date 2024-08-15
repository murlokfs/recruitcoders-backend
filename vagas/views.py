from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from .models import Vaga, Stack, Local, Empresa
from .filters import VagaFilter

class Index(TemplateView):
    template_name = "index.html"

class VagaListView(ListView):
    model = Vaga
    template_name = "vagas.html"
    context_object_name = "vagas"

    def get_queryset(self):
        queryset = Vaga.objects.filter(is_ativo=True)
        filter = VagaFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = VagaFilter(self.request.GET, self.get_queryset())
        context["locais"] = Local.objects.all()
        context["f_contratos"] = self.request.GET.getlist('contrato')
        context["f_experiencias"] = self.request.GET.getlist('experiencia')
        return context

    
    