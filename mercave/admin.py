from django.contrib import admin

from .models import Organizacion, Diseñador, Fabricante, Mantenedor, Keeper, Operador, Aprovador, Certificador
from .models import Composicion, Vagon, VersionEje, Eje, VersionCambiador, Cambiador
from .models import Cambio, Circulacion, AlarmaCambio, AlarmaCirculacion, Linea, PuntoRed, Inicio,Final

# Register your models here.
admin.site.register(Organizacion)
admin.site.register(Diseñador)
admin.site.register(Fabricante)
admin.site.register(Mantenedor)
admin.site.register(Keeper)
admin.site.register(Operador)
admin.site.register(Aprovador)
admin.site.register(Certificador)
admin.site.register(Composicion)
admin.site.register(Vagon)
admin.site.register(VersionEje)
admin.site.register(Eje)
admin.site.register(VersionCambiador)
admin.site.register(Cambiador)
admin.site.register(Cambio)
admin.site.register(Circulacion)
admin.site.register(AlarmaCambio)
admin.site.register(AlarmaCirculacion)
admin.site.register(Linea)
admin.site.register(PuntoRed)
admin.site.register(Inicio)
admin.site.register(Final)
