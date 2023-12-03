# En el archivo mi_aplicacion/models.py

from django.db import models

class PaginaWeb(models.Model):
    url = models.URLField(unique=True)
   

class Parrafo(models.Model):
    pagina_web = models.ForeignKey(PaginaWeb, on_delete=models.CASCADE)
    texto = models.TextField()
    

class AnalisisTexto(models.Model):
    parrafo = models.ForeignKey(Parrafo, on_delete=models.CASCADE)
    tokens = models.JSONField()
    tagged = models.JSONField()
    summary = models.TextField()
    
