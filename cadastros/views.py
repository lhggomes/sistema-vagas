from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
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


# For Deleting values
class VagaDelete(DeleteView):
    model = PCVaga
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')



class VagaList(ListView):
    model = PCVaga
    template_name = 'cadastros/listas/vaga.html'
