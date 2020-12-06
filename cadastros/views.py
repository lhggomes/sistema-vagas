from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import PCEmpresa, PCVaga, PCCandidato, PCCandidatura


class VagaCreate(CreateView):
    model = PCVaga
    fields = ['descricao', 'salario', 'requisitos', 'escolaridade', 'empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class CandidatoCreate(CreateView):
    model = PCCandidato
    fields = ['nome', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class EmpresaCreate(CreateView):
    model = PCEmpresa
    fields = ['razao_social', 'cnpj']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class CandidaturaCrate(CreateView):
    model = PCCandidatura
    fields = ['candidato', 'vaga', 'experiencia', 'ultima_escolaridade', 'pretensao_salarial']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


# For Updating the values

class VagaUpdate(UpdateView):
    model = PCVaga
    fields = ['descricao', 'salario', 'requisitos', 'escolaridade', 'empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
