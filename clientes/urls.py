from django.urls import path
from .views import meus_eventos, meus_certificados



urlpatterns = [
    path('meus_eventos/', meus_eventos, name='meus_eventos'),
    path('meus_certificados/', meus_certificados, name='meus_certificados'),
]