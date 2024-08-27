from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django_filters.views import FilterView

from .filters import CandidaturaFilter, VagaFilter
from .forms import CurriculoForm, VagaForm
from .models import Candidatura, Curriculo, Vaga


class Index(TemplateView):
    template_name = "index.html"


class VagaListView(FilterView):
    model = Vaga
    template_name = "vagas.html"
    context_object_name = "vagas"
    filterset_class = VagaFilter
    paginate_by = 4

    def get_queryset(self):
        if cache.get("c_queryset") is None:
            c_queryset = (
                Vaga.objects.select_related("empresa", "local")
                .filter(is_ativo=True)
                .order_by("-criado_em")
            )
            cache.set(
                "c_queryset", c_queryset, timeout=30
            )  # cache da queryset da pagina de listagem de vagas onde a cada 30s renova
        queryset = cache.get("c_queryset")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = VagaFilter(self.request.GET, self.get_queryset())
        context["stacks"] = Vaga.STACKS

        context["f_contratos"] = self.request.GET.getlist("contrato")
        context["f_experiencias"] = self.request.GET.getlist("experiencia")
        context["f_stacks"] = self.request.GET.getlist("stack")

        if cache.get("now") is None:
            now = datetime.now().strftime("%H:%M:%S")
            cache.set("now", now, timeout=5)

        context["now"] = cache.get("now")
        return context


class VagaDetailView(DetailView):
    model = Vaga
    context_object_name = "vaga"
    template_name = "vaga-detalhe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["is_candidato"] = (
                Candidatura.objects.select_related("vaga")
                .filter(candidato=self.request.user, vaga=self.get_object())
                .exists()
            )
        else:
            context["is_candidato"] = False
        return context


class CurriculoCreateView(LoginRequiredMixin, CreateView):
    model = Curriculo
    form_class = CurriculoForm
    template_name = "forms/curriculo.html"
    success_url = reverse_lazy("vaga-list-page")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def dispatch(
        self, request, *args, **kwargs
    ):  # caso o usuario ja possua um curriculo cadastrado, ele é redirecionado para curriculo update
        if (
            Curriculo.objects.select_related("usuario")
            .filter(usuario=request.user)
            .exists()
        ):
            return redirect(
                "curriculo-update",
                pk=Curriculo.objects.get(usuario=request.user).id,
            )
        return super().dispatch(request, *args, **kwargs)


class CurriculoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curriculo
    form_class = CurriculoForm
    template_name = "forms/curriculo.html"
    success_url = reverse_lazy("vaga-list-page")

    def get_queryset(
        self,
    ):  # query set só vai retornar o curriculo o qual o usuario preenche o campo de "usuario", se tornando impossivel acessar outros curriculos via id
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
        queryset = (
            Candidatura.objects.select_related("vaga")
            .filter(candidato=self.request.user)
            .order_by("vaga")
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = VagaFilter(self.request.GET, self.get_queryset())
        context[
            "stacks"
        ] = Vaga.STACKS  # retorno da lista de choices de stacks do models

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
                progresso = (
                    candidatura.etapa / candidatura.vaga.qntd_etapas
                ) * 100
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

        if not Curriculo.objects.filter(
            usuario=usuario
        ).exists():  # caso o usuário não tenha curriculo cadastrado ainda, direciona ele para a página curriculo
            return redirect("curriculo")

        if (
            Candidatura.objects.filter(vaga=vaga, candidato=usuario).exists()
            or vaga.is_ativo == False
        ):  # caso o usuario ja tenha se candidatado na vaga, direciona ele pra pagina de sucesso sem fazer o POST
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


# DASHBOARD -


class DashboardListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Vaga
    template_name = "dashboard/dashboard.html"
    context_object_name = "vagas"

    def get_queryset(self):
        return Vaga.objects.filter(empresa=self.request.user.empresa)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empresa = self.request.user.empresa

        total_vagas = Vaga.objects.filter(empresa=empresa).count()
        total_candidaturas = Candidatura.objects.filter(
            vaga__empresa=empresa
        ).count()
        vagas_ativas = Vaga.objects.filter(
            empresa=empresa, is_ativo=True
        ).count()
        vagas_encerradas = Vaga.objects.filter(
            empresa=empresa, is_ativo=False
        ).count()

        context["total_vagas"] = total_vagas
        context["total_candidaturas"] = total_candidaturas
        context["vagas_ativas"] = vagas_ativas
        context["vagas_encerradas"] = vagas_encerradas

        return context

    def test_func(self):
        return self.request.user.groups.filter(name="Empresa").exists()


class DashboardCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vaga
    form_class = VagaForm
    template_name = "dashboard/vaga-form.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.empresa = self.request.user.empresa
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.groups.filter(name="Empresa").exists()


class DashboardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vaga
    form_class = VagaForm
    template_name = "dashboard/vaga-form.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.empresa = self.request.user.empresa
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.groups.filter(name="Empresa").exists()


class DashboardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vaga
    template_name = "dashboard/vaga-delete.html"
    success_url = reverse_lazy("dashboard")

    def test_func(self):
        return self.request.user.groups.filter(name="Empresa").exists()


class DashboardCandidaturasListView(
    LoginRequiredMixin, UserPassesTestMixin, ListView
):
    model = Candidatura
    template_name = "dashboard/vaga-view.html"
    context_object_name = "candidaturas"

    def get_queryset(self):
        vaga_id = self.kwargs["pk"]
        if cache.get("c_queryset") is None:
            c_queryset = Candidatura.objects.select_related("vaga").filter(
                vaga=get_object_or_404(Vaga, id=vaga_id)
            )
            cache.set(
                "c_queryset", c_queryset, timeout=2
            )  # cache da queryset da pagina de listagem de vagas onde a cada 30s renova
        queryset = cache.get("c_queryset")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if cache.get("now") is None:
            now = datetime.now().strftime("%H:%M:%S")
            cache.set("now", now, timeout=30)

        context["now"] = cache.get("now")
        return context

    def test_func(self):
        vaga = get_object_or_404(Vaga, id=self.kwargs["pk"])
        return (
            self.request.user.groups.filter(name="Empresa").exists()
            and vaga.empresa.usuario == self.request.user
        )
