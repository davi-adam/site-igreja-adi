from django.db import models
from django.core.exceptions import ValidationError

CATEGORIA_CHOICES = [
    ('culto', 'Culto'),
    ('retiro', 'Retiro'),
    ('reuniao', 'Reunião'),
    ('outro', 'Outro'),
]

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    local = models.CharField(max_length=200)
    vagas_maximas = models.PositiveIntegerField(null=True, blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='outro')

    def __str__(self):
        return self.titulo

    def clean(self):
        if self.data_fim and self.data_inicio and self.data_fim < self.data_inicio:
            raise ValidationError("A data de fim não pode ser anterior à data de início.")