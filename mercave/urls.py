from django.urls import path
from .views import VistaComposicion, VistaEjes, VistaCambiadores, VistaComposiciones, VistaEje, VistaCambiador

urlpatterns = [
    path("", VistaEjes, name ='ejes_expl'),
    path("ejes/", VistaEjes, name ='ejes_expl'),
    path("cambiadores/", VistaCambiadores, name ='cambiadores_expl'),
    path("composiciones/", VistaComposiciones, name ='composiciones_expl'),
    path("eje/<int:pk>/", VistaEje, name ='ficha_eje'),
    path("cambiador/<int:pk>/", VistaCambiador, name ='ficha_cambiador'),
    path("composicion/<int:pk>/", VistaComposicion, name ='ficha_composicion'),
]
