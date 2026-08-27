from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_inicio', 'data_fim', 'local', 'vagas_maximas', 'categoria')
    search_fields = ('titulo', 'local')
    list_filter = ('data_inicio', 'categoria')
    ordering = ('data_inicio',)
    date_hierarchy = 'data_inicio'
    fieldsets = (
        ('Informações do Evento', {
            'fields': ('titulo', 'descricao', 'categoria')
        }),
        ('Data e Local', {
            'fields': ('data_inicio', 'data_fim', 'local')
        }),
        ('Inscrições', {
            'fields': ('vagas_maximas',)
        }),
    )