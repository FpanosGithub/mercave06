from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Fabricante, Mantenedor, Keeper, Operador, Composicion, Vagon, Bogie, Eje, Cambiador, Cambio, CirculacionEje, CirculacionComposicion, CirculacionVagon, AlarmaCambio, AlarmaCirculacion
from .mapas import mapa_ejes, mapa_cambiadores, mapa_vagones, mapa_bogies, mapa_composiciones, mapa_cambiador, mapa_eje, mapa_cambios, mapa_vagon, mapa_composicion, mapa_bogie, mapa_posicionar
from .graficas import  plotear_alarma_circulacion, plotear_cambios
from .logistica_ferroviaria import Pruebas

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Vista de pueba de lógicas 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def PruebasLogistica (request):
    Pruebas()
    return render(request, 'prueba.html')

# Create your views here.
@login_required
def VistaEjes(request):
    fabricantes = Fabricante.objects.filter(de_ejes = True)
    mantenedores = Mantenedor.objects.filter(de_ejes = True)
    keepers = Keeper.objects.filter()
    operadores = Operador.objects.filter()
    ejes = Eje.objects.all()
    mapa = mapa_ejes(ejes)
    
    return render(request, 'ejes_explotacion.html', context={
                    'mapa':mapa,
                    'fabricantes':fabricantes,
                    'mantenedores':mantenedores,
                    'keepers':keepers,
                    'operadores':operadores,
                    'ejes':ejes})

#@login_required
def VistaCambiadores(request):
    fabricantes = Fabricante.objects.filter(de_cambiadores = True)
    mantenedores = Mantenedor.objects.filter(de_cambiadores = True)
    cambiadores = Cambiador.objects.all()
    mapa = mapa_cambiadores(cambiadores)

    return render(request, 'cambiadores_explotacion.html', context={
                    'mapa':mapa, 
                    'fabricantes':fabricantes, 
                    'mantenedores':mantenedores, 
                    'cambiadores':cambiadores})

#@login_required
def VistaVagones(request):
    vagones = Vagon.objects.all()
    mapa = mapa_vagones(vagones)
    
    return render(request, 'vagones_explotacion.html', context={
                    'mapa':mapa,
                    'vagones':vagones})

#@login_required
def VistaBogies(request):
    bogies = Bogie.objects.all()
    mapa = mapa_bogies(bogies)
    
    return render(request, 'bogies_explotacion.html', context={
                    'mapa':mapa,
                    'bogies':bogies})


#@login_required
def VistaComposiciones(request):
    composiciones = Composicion.objects.all()
    mapa = mapa_composiciones(composiciones)

    return render(request, 'composiciones_explotacion.html', context={
                    'mapa':mapa, 
                    'composiciones':composiciones, 
                    })

#@login_required
def VistaEje(request, pk):
    eje_ficha = Eje.objects.get(pk=pk)
    cambios = Cambio.objects.filter(eje=eje_ficha)
    circulaciones = CirculacionEje.objects.filter(eje=eje_ficha)[:5]
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
    
    return render(request, 'ficha_cambiador.html', context={
                    'cambiador':cambiador_ficha, 
                    'cambios': cambios, 
                    'grd':grd, 
                    'grc':grc, 
                    'gre':gre, 
                    'mapa':mapa})

#@login_required
def VistaVagon(request, pk):
    vagon_ficha = Vagon.objects.get(pk=pk)
    circulaciones = CirculacionVagon.objects.filter(vagon=vagon_ficha)[:6]
    bogies = Bogie.objects.filter(vagon = vagon_ficha)
    ejes = Eje.objects.filter(vagon = vagon_ficha)
    mapa_situacion_vagon = mapa_vagon(vagon_ficha, circulaciones)
    
    return render(request, 'ficha_vagon.html', context={
                    'vagon':vagon_ficha, 
                    'circulaciones':circulaciones,
                    'bogies': bogies,
                    'ejes':ejes,
                    'mapa':mapa_situacion_vagon},)

#@login_required
def VistaBogie(request, pk):
    bogie_ficha = Bogie.objects.get(pk=pk)
    ejes = Eje.objects.filter(bogie = bogie_ficha)
    mapa_situacion_bogie = mapa_bogie(bogie_ficha)
    
    return render(request, 'ficha_bogie.html', context={
                    'bogie':bogie_ficha, 
                    'ejes':ejes,
                    'mapa':mapa_situacion_bogie},)


#@login_required
def VistaComposicion(request, pk):
    composicion_ficha = Composicion.objects.get(pk=pk)
    circulaciones = CirculacionComposicion.objects.filter(composicion=composicion_ficha)[:6]
    vagones = Vagon.objects.filter(composicion=composicion_ficha)
    ##
    lista_vagones = []
    for vagon in vagones:
        lista_vagones.append(vagon.pk)
    ##
    ejes = Eje.objects.filter(vagon__pk__in=lista_vagones)
    mapa_situacion_composicion = mapa_composicion(composicion_ficha, circulaciones)
    
    return render(request, 'ficha_composicion.html', context={
                    'composicion':composicion_ficha, 
                    'circulaciones':circulaciones,
                    'vagones': vagones,
                    'ejes':ejes,
                    'mapa':mapa_situacion_composicion},)

#@login_required
def VistaMapa(request):
    mapa = mapa_posicionar()
    return render(request, 'mapa_posicionar.html', context={'mapa':mapa,})