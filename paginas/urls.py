from django.urls import path
from .views import IndexView, SobreView, VagaView

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('vagas/', VagaView.as_view(), name='vaga')
]
