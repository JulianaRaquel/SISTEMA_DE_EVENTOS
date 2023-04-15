from django.urls import path
from .views import novo_evento, gerenciar_evento, inscrever_evento, participantes_evento, gerar_csv, certificados_evento, gerar_certificado



urlpatterns = [
    path('novo_evento/', novo_evento, name='novo_evento'),
    path('gerenciar_evento/', gerenciar_evento, name="gerenciar_evento"),
    path('inscrever_evento/<int:id>', inscrever_evento, name='inscrever_evento'),
    path('participantes_evento/<int:id>', participantes_evento, name='participantes_evento'),
    path('gerar_csv/<int:id>', gerar_csv, name='gerar_csv'),
    path('certificados_evento/<int:id>', certificados_evento, name="certificados_evento"),
    path('gerar_certificado/<int:id>', gerar_certificado, name='gerar_certificado'),
]