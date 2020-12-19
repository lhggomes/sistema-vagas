from django.urls import path
from .views import IndexView, SobreView, VagaView, PrimeirosPassosView, DashboardView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('vagas/', VagaView.as_view(), name='vaga'),
    path('primeiros-passos/', PrimeirosPassosView.as_view(), name='primeiros-passos'),
    path('empresa/dashboard/', DashboardView.as_view(), name='dashboard'),
]

