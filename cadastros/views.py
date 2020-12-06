from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Empresa, Vaga, Candidato, Candidatura

class VagaCreate(CreateView):
    model = Vaga
    fields = ['descricao', 'salario', 'requisitos', 'escolaridade', 'empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class CandidatoCreate(CreateView):
    model = Candidato
    fields = ['nome', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
