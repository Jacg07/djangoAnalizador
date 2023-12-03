from django.urls import path
from .views import analisis_texto

urlpatterns = [
    path('analisis_texto/', analisis_texto, name='analisis_texto'),
]
