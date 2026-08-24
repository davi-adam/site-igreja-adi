from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    local = models.CharField(max_length=200)
    vagas_maximas = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo
    