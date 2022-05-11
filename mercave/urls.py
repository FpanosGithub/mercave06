from django.urls import path
from .views import VistaComposicion, VistaEjes, VistaCambiadores, VistaVagon, VistaVagones, VistaComposiciones, VistaEje, VistaCambiador, VistaVagones
from .views import PruebasLogistica

urlpatterns = [
    path("", VistaEjes, name ='ejes_expl'),
    path("ejes/", VistaEjes, name ='ejes_expl'),
    path("cambiadores/", VistaCambiadores, name ='cambiadores_expl'),
    path("vagones/", VistaVagones, name ='vagones_expl'),
    path("composiciones/", VistaComposiciones, name ='composiciones_expl'),
    path("eje/<int:pk>/", VistaEje, name ='ficha_eje'),
    path("cambiador/<int:pk>/", VistaCambiador, name ='ficha_cambiador'),
    path("vagon/<int:pk>/", VistaVagon, name ='ficha_vagon'),
    path("composicion/<int:pk>/", VistaComposicion, name ='ficha_composicion'),
    path("prueba/", PruebasLogistica, name = 'pruebas_logistica')
]
