from django.urls import path
from .views import CandidatoCreate, VagaCreate

urlpatterns = [
   path('cadastrar/candidato/', CandidatoCreate.as_view(), name="cad-candidato"),
   path('cadastrar/vaga/', VagaCreate.as_view(), name="cad-vaga"),
]
