from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_inicio', 'data_fim', 'local', 'vagas_maximas')
    search_fields = ('titulo', 'local')
    list_filter = ('data_inicio',)