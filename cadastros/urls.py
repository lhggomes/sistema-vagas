from django.urls import path
from .views import CandidatoCreate, VagaCreate, CandidaturaCrate, VagaUpdate, EmpresaCreate
from .views import VagaDelete
from .views import VagaList

urlpatterns = [
    path('cadastrar/candidato/', CandidatoCreate.as_view(), name="cad-candidato"),
    path('cadastrar/vaga/', VagaCreate.as_view(), name="cad-vaga"),
    path('cadastrar/empresa/', EmpresaCreate.as_view(), name="cad-empresa"),
    path('cadastrar/candidatura', CandidaturaCrate.as_view(), name="cad-candidatura"),

    path('editar/vaga/<int:pk>', VagaUpdate.as_view(), name="editar-vaga"),

    path('excluir/vaga/<int:pk>', VagaDelete.as_view(), name="excluir-vaga"),

    path('listar/vagas/', VagaList.as_view(), name="listar-vagas"),

]
