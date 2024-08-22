from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    TemplateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .models import Vaga, Local, Empresa, Candidatura, Curriculo
from .filters import VagaFilter, CandidaturaFilter
from django.urls import reverse_lazy
from .forms import CurriculoForm


class Index(TemplateView):
    template_name = "index.html"

class VagaListView(FilterView):
    model = Vaga
    template_name = "vagas.html"
    context_object_name = "vagas"
    filterset_class = VagaFilter
    paginate_by = 4

    def get_queryset(self):
        queryset = Vaga.objects.filter(is_ativo=True).order_by("-criado_em")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = VagaFilter(self.request.GET, self.get_queryset())
        context["stacks"] = Vaga.STACKS

        context["f_contratos"] = self.request.GET.getlist("contrato")
        context["f_experiencias"] = self.request.GET.getlist("experiencia")
        context["f_stacks"] = self.request.GET.getlist("stack")
        return context


class VagaDetailView(DetailView):
    model = Vaga
    context_object_name = "vaga"
    template_name = "vaga-detalhe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_candidato"] = Candidatura.objects.filter(candidato=self.request.user, vaga=self.get_object()).exists()
        return context


class CurriculoCreateView(CreateView):
    model = Curriculo
    form_class = CurriculoForm
    template_name = "forms/curriculo.html"
    success_url = reverse_lazy("vaga-list-page")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs): # caso o usuario ja possua um curriculo cadastrado, ele é redirecionado para curriculo update
        if Curriculo.objects.filter(usuario=request.user).exists():
            return redirect(
                "curriculo-update",
                pk=Curriculo.objects.get(usuario=request.user).id,
            )
        return super().dispatch(request, *args, **kwargs)


class CurriculoUpdateView(UpdateView):
    model = Curriculo
    form_class = CurriculoForm
    template_name = "forms/curriculo.html"
    success_url = reverse_lazy("vaga-list-page")

    def get_queryset(self): # query set só vai retornar o curriculo o qual o usuario preenche o campo de "usuario", se tornando impossivel acessar outros curriculos via id
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)


class CandidaturaListView(LoginRequiredMixin, FilterView):
    model = Candidatura
    template_name = "candidaturas.html"
    context_object_name = "candidaturas"
    filterset_class = CandidaturaFilter
    paginate_by = 4

    def get_queryset(self):
        # queryset de candidaturas, 
        queryset = Candidatura.objects.filter(
            candidato=self.request.user, is_ativa=True
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = VagaFilter(self.request.GET, self.get_queryset())
        context["stacks"] = Vaga.STACKS #retorno da lista de choices de stacks do models

        # criei essa solucao para conseguir fazer a leitura do filtro ativo durante uma filtragem, usei esses recursos na persistencia dos campos de filtro (checkbox)
        # ao filtrar, os checkboxs estavam esvaziando, mesmo com o filtro ativo. então na template há uma checagem do filtro ativo, caso estiver, o campo relacionado ficará marcado na atualização da página.
        context["f_contratos"] = self.request.GET.getlist("contrato")
        context["f_experiencias"] = self.request.GET.getlist("experiencia")
        context["f_stacks"] = self.request.GET.getlist("stack")

        # criei essa solucao para suprir a necessidade de retornar uma variável que informasse o progresso do usuário na vaga em porcentagem
        # utilizei desse recurso para estilização, aplicando a porcentagem em um width da barra de progresso no css. 
        for candidatura in context["candidaturas"]:
            progresso = 0
            if candidatura.vaga.qntd_etapas > 0:
                progresso = (candidatura.etapa / candidatura.vaga.qntd_etapas) * 100
                progresso = int(progresso)
            candidatura.progresso = progresso
        return context


class CandidaturaCreateView(LoginRequiredMixin, CreateView):
    model = Candidatura
    fields = []
    template_name = "forms/candidatura-confirm.html"
    success_url = reverse_lazy("candidaturas")

    def form_valid(self, form):
        vaga = get_object_or_404(Vaga, id=self.kwargs["vaga_id"])
        usuario = self.request.user

        if not Curriculo.objects.filter(usuario=usuario).exists(): #caso o usuário não tenha curriculo cadastrado ainda, direciona ele para a página curriculo
            return redirect("curriculo")
        
        if Candidatura.objects.filter(vaga=vaga, candidato=usuario).exists() or vaga.is_ativo == False: #caso o usuario ja tenha se candidatado na vaga, direciona ele pra pagina de sucesso sem fazer o POST
            # print('post nao saiu')
            return redirect(self.success_url)
        else:
            form.instance.vaga = vaga
            form.instance.candidato = usuario
            form.instance.etapa = 1
            form.instance.is_ativa = True
            # print("post saiu")
            return super().form_valid(form)


class CandidaturaDeleteView(LoginRequiredMixin, DeleteView):
    model = Candidatura
    template_name = "forms/candidatura-delete.html"
    success_url = reverse_lazy("candidaturas")
