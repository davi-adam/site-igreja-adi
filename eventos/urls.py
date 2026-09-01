from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendario, name='calendario'),
    path('json/', views.eventos_json, name='eventos_json'),
    path('<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
]