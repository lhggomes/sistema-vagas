from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import PCEmpresa, PCVaga, PCCandidato, PCCandidatura


# Create Views
class VagaCreate(CreateView):
    model = PCVaga
    fields = ['descricao', 'salario', 'requisitos', 'escolaridade', 'empresa']
    template_name = 'cadastros/form.html'
    success_message = 'Vaga criada com sucesso!'
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        return super().form_invalid(form)


class CandidatoCreate(CreateView):
    model = PCCandidato
    fields = ['nome', 'email']
    template_name = 'cadastros/form.html'
    success_message = 'Cadastro realizado com sucesso!'
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        return super().form_invalid(form)


class EmpresaCreate(CreateView):
    model = PCEmpresa
    fields = ['razao_social', 'cnpj']
    template_name = 'cadastros/form.html'
    success_message = 'Empresa criada com sucesso!'
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        return super().form_invalid(form)


class CandidaturaCrate(CreateView):
    model = PCCandidatura
    fields = ['candidato', 'vaga', 'experiencia', 'ultima_escolaridade', 'pretensao_salarial']
    template_name = 'cadastros/form.html'
    success_message = 'Candidatura confirmada com sucesso!'
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        return super().form_invalid(form)


# For Updating the values

class VagaUpdate(UpdateView):
    model = PCVaga
    fields = ['descricao', 'salario', 'requisitos', 'escolaridade', 'empresa']
    template_name = 'cadastros/form.html'
    success_message = 'Vaga atualizada com sucesso!'
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        return super().form_invalid(form)


# For Deleting values
class VagaDelete(DeleteView):
    model = PCVaga
    template_name = 'cadastros/form-excluir.html'
    success_message = 'Vaga apagada com sucesso'
    success_url = reverse_lazy('index')


class VagaList(ListView):
    model = PCVaga
    template_name = 'cadastros/listas/vaga.html'


class CandidaturaView(DetailView):
    model = PCCandidatura
    template_name = 'cadastros/listas/vaga-info.html'


class VagasDashboardView(ListView):
    model = PCVaga
    template_name = 'cadastros/dashboard/vagas.html'


class CandidatoDashboardView(ListView):
    model = PCCandidato
    template_name = 'cadastros/dashboard/candidatos.html'
