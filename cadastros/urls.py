from django.urls import path
from .views import CandidatoCreate, VagaCreate, CandidaturaCrate, VagaUpdate

urlpatterns = [
    path('cadastrar/candidato/', CandidatoCreate.as_view(), name="cad-candidato"),
    path('cadastrar/vaga/', VagaCreate.as_view(), name="cad-vaga"),
    path('cadastrar/candidatura', CandidaturaCrate.as_view(), name="cad-candidatura"),

    path('editar/campo/<int:pk>', VagaUpdate.as_view(), name="editar-campo"),
]
