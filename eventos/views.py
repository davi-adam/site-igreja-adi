from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Evento
import logging

logger = logging.getLogger(__name__)

CORES = {
    'culto': '#4fa38a',
    'retiro': '#9b7fc7',
    'reuniao': '#d8a24a',
    'outro': '#73726c',
}
def calendario(request):
   return render(request, 'calendario.html')

def detalhe_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    return render(request, 'detalhe_evento.html', {
        'evento': evento
    })

def eventos_json(request):
    try:
        eventos = Evento.objects.all()
        dados = [
            {
                'id': e.id,
                'title': e.titulo,
                'start': e.data_inicio.isoformat(),
                'end': e.data_fim.isoformat(),  
                'color': CORES.get(e.categoria, '#73726c'),
                'url': f'/eventos/{e.id}/',
                'extendedProps': {'local': e.local},
            }
            for e in eventos
        ]
        return JsonResponse(dados, safe=False)
    except Exception as e:
        logger.error(f"Erro ao carregar eventos: {e}")
        return JsonResponse({'erro': 'Não foi possível carregar os eventos.'}, status=500)