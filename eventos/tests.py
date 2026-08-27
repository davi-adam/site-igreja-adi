from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Evento

class EventoJsonViewTest(TestCase):
    def setUp(self):
        self.evento = Evento.objects.create(
            titulo='Culto de Domingo',
            data_inicio=timezone.now(),
            data_fim=timezone.now() + timedelta(hours=2),
            local='Templo Principal',
            categoria='culto',
        )

    def test_eventos_json_retorna_200(self):
        response = self.client.get(reverse('eventos_json'))
        self.assertEqual(response.status_code, 200)

    def test_eventos_json_contem_evento_criado(self):
        response = self.client.get(reverse('eventos_json'))
        dados = response.json()
        titulos = [e['title'] for e in dados]
        self.assertIn('Culto de Domingo', titulos)