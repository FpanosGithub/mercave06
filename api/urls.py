from django.urls import path
from api.views import lista_composiciones, detalle_composiciones, mover_composiciones

urlpatterns = [
    path("composiciones/", lista_composiciones, name ='lista_composiciones'),
    path("composiciones/<int:pk>/", detalle_composiciones, name ='detalle_composiciones'),
    path("composiciones/mover/<int:pk>/", mover_composiciones, name ='mover_composicion'),
]