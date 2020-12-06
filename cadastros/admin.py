from django.contrib import admin
from .models import Empresa, Vaga, Candidato, Candidatura

admin.site.register(Empresa)
admin.site.register(Vaga)
admin.site.register(Candidato)
admin.site.register(Candidatura)
