from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Fabricante, Mantenedor, Keeper, Operador, Eje, Cambiador, Cambio, Circulacion, AlarmaCambio, AlarmaCirculacion
from .gis import mapa_ejes, mapa_cambiadores, mapa_cambiador, mapa_eje, mapa_cambios, plotear_alarma_circulacion, plotear_cambios

# Create your views here.
#@login_required
def VistaEjes(request):
    fabricantes = Fabricante.objects.filter(de_ejes = True)
    mantenedores = Mantenedor.objects.filter(de_ejes = True)
    keepers = Keeper.objects.filter()
    operadores = Operador.objects.filter()
    ejes = Eje.objects.all()
    mapa = mapa_ejes(ejes)

    return render(request, 'ejes_explotacion.html', context={'mapa':mapa, 'fabricantes':fabricantes, 'mantenedores':mantenedores, 'keepers':keepers, 'operadores':operadores, 'ejes':ejes})

#@login_required
def VistaCambiadores(request):
    fabricantes = Fabricante.objects.filter(de_cambiadores = True)
    mantenedores = Mantenedor.objects.filter(de_cambiadores = True)
    cambiadores = Cambiador.objects.all()
    mapa = mapa_cambiadores(cambiadores)

    return render(request, 'cambiadores_explotacion.html', context={'mapa':mapa, 'fabricantes':fabricantes, 'mantenedores':mantenedores, 'cambiadores':cambiadores})

#@login_required
def VistaEje(request, pk):
    eje_ficha = Eje.objects.get(pk=pk)
    cambios = Cambio.objects.filter(eje=eje_ficha)
    circulaciones = Circulacion.objects.filter(eje=eje_ficha)[:5]
    alarmas_circulacion = AlarmaCirculacion.objects.filter(circulacion__eje__pk=eje_ficha.pk)
    alarmas_cambios = AlarmaCambio.objects.filter(cambio__eje__pk=eje_ficha.pk)
    mapa_situacion_eje = mapa_eje(eje_ficha, circulaciones)
    mapa_cambios_eje = mapa_cambios(cambios)
    grd, grc, gre = plotear_cambios(cambios)

    return render(request, 'ficha_eje.html', context=
                    {'eje':eje_ficha,
                    'mapa_eje':mapa_situacion_eje, 
                    'cambios':cambios, 
                    'circulaciones':circulaciones, 
                    'mapa_cambios':mapa_cambios_eje, 
                    'alarmas_circulacion': alarmas_circulacion, 
                    'alarmas_cambios': alarmas_cambios,
                    'grd':grd,
                    'grc':grc,
                    'gre':gre,
                    })

#@login_required
def VistaCambiador(request, pk):
    cambiador_ficha = Cambiador.objects.get(pk=pk)
    cambios = Cambio.objects.filter(cambiador=cambiador_ficha)
    grd, grc, gre = plotear_cambios(cambios)
    mapa = mapa_cambiador(cambiador_ficha)
    
    return render(request, 'ficha_cambiador.html', context={'cambiador':cambiador_ficha, 'cambios': cambios, 'grd':grd, 'grc':grc, 'gre':gre, 'mapa':mapa})