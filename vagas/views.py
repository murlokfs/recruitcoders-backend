from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .models import Vaga, Local, Empresa, Candidatura
from .filters import VagaFilter, CandidaturaFilter

class Index(TemplateView):
    template_name = "index.html"

class VagaListView(FilterView):
    model = Vaga
    template_name = "vagas.html"
    context_object_name = "vagas"
    filterset_class = VagaFilter
    paginate_by = 4

    def get_queryset(self):
        queryset = Vaga.objects.filter(is_ativo=True).order_by('-criado_em')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = VagaFilter(self.request.GET, self.get_queryset())
        context["stacks"] = Vaga.STACKS

        context["f_contratos"] = self.request.GET.getlist('contrato')
        context["f_experiencias"] = self.request.GET.getlist('experiencia')
        context["f_stacks"] = self.request.GET.getlist('stack')
        return context
    
class VagaDetailView(DetailView):
    model = Vaga
    context_object_name = "vaga"
    template_name = "vaga-detalhe.html"

class CandidaturaListView(LoginRequiredMixin,FilterView):
    model = Candidatura
    template_name = "candidaturas.html"
    context_object_name = "candidaturas"
    filterset_class = CandidaturaFilter
    paginate_by = 4

    def get_queryset(self):
        queryset = Candidatura.objects.filter(candidato=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = VagaFilter(self.request.GET, self.get_queryset())
        context["stacks"] = Vaga.STACKS

        context["f_contratos"] = self.request.GET.getlist('contrato')
        context["f_experiencias"] = self.request.GET.getlist('experiencia')
        context["f_stacks"] = self.request.GET.getlist('stack')

        for candidatura in context["candidaturas"]:
            progresso = 0
            if candidatura.vaga.qntd_etapas > 0:
                progresso = (candidatura.etapa / candidatura.vaga.qntd_etapas) * 100
                progresso = int(progresso)
            candidatura.progresso = progresso
        return context

    