from django.contrib import admin

from .models import PCEmpresa, PCVaga, PCCandidato, PCCandidatura

admin.site.register(PCEmpresa)
admin.site.register(PCVaga)
admin.site.register(PCCandidato)
admin.site.register(PCCandidatura)
