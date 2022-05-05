from django.urls import path
from .views import HomePage, VistaEjes, VistaCambiadores, VistaEje, VistaCambiador

urlpatterns = [
    path("", HomePage,name ='home'),
    path("ejes/", VistaEjes, name ='ejes_expl'),
    path("cambiadores/", VistaCambiadores, name ='cambiadores_expl'),
    path("eje/<int:pk>/", VistaEje, name ='ficha_eje'),
    path("cambiador/<int:pk>/", VistaCambiador, name ='ficha_cambiador'),
]
