# En el archivo mi_aplicacion/admin.py
from django.contrib import admin
from .models import PaginaWeb, Parrafo, AnalisisTexto

admin.site.register(PaginaWeb)
admin.site.register(Parrafo)
admin.site.register(AnalisisTexto)
