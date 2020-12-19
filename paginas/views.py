from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'paginas/index.html'


class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'


class VagaView(TemplateView):
    template_name = 'paginas/vagas.html'


class PrimeirosPassosView(TemplateView):
    template_name = 'paginas/primeiros.html'


class DashboardView(TemplateView):
    template_name = 'paginas/administrador.html'
