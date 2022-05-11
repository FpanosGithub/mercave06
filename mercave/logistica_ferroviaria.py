from .models import Composicion, Vagon, Bogie, Eje, CirculacionEje, CirculacionComposicion, Operador

# Operaciones de movimiento de material rodante.
# La localización de destino deberá ser un dict con 2 keys {'lng': x, 'lat: y} 
# Al mover una composición automáticamente se mueven los vagones, bogies y ejes asociados.
# Creamos funciones para mover vagones y Bogies. Estos solo podrán moverse si la composición 
# a la que están asociados está ya en lugar de destino o no están asociados a una composición

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Fuciones para probar las lógicas de este módulo
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def Pruebas ():
    # Varios destinos para jugar
    destino1 = {'lugar': 'León','lng': -5.5801,'lat': 42.5772,}
    destino2 = {'lugar': 'Tarragona','lng': 1.2053,'lat': 41.0982,}
    destino3 = {'lugar': 'Gabaldón','lng': -1.9472,'lat': 39.635,}
    destino4 = {'lugar': 'Miranda','lng': -2.9395,'lat': 42.6919}
    destino5 = {'lugar': 'Madrid','lng': -3.982,'lat': 40.2951,}
    data_composicion_Adif = {'codigo':'Adif-0001', 'descripcion':'Tren de pruebas de Mercave', 'operador':'Adif'}
    data_composicion_Renfe = {'codigo':'RENFE291', 'descripcion':'', 'operador':'Renfe'}
    data_composicion_sncf = {'codigo':'Sncf-0001', 'descripcion':'allors enfants de la patrie', 'operador':'Sncf'}
    lista_vagones = ['RENFE2345']
    lista_bogies = ['RENFE1345', 'RENFE1348', 'ADIF001', 'ADIF002', 'ADIF003', 'ADIF004']
    lista_ejes = ['TR0001','TR0002','TR0003','TR0004','TR0005','TR0006','TR0007','TR0008','TR0009','TR0010','TR0011','TR0012','TR0013','TR0014','TR0015','TR0016',]
    
    # Pruebas varias
    formar_composicion(data_composicion_Renfe,destino3, lista_vagones)

    
    


    
    
    
    
    


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Funciones para mover elementos de un sitio a otro
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def mover_bogie(bogie, destino):
    # Movemos el bogie a nuevo lugar
    bogie.mover(destino)
    ejes = Eje.objects.filter(bogie = bogie)
    for eje in ejes:
        eje.mover(destino)

def mover_vagon(vagon, destino):
    # Comprobamos si pertenece a una composición y esta ha sido movida ya a la localización de destino
    # Si esta función viene llamada desde mover_composicion es redundante preguntar si la composicion
    # esta posicionada pero si la función se llama desde otro punto, no queremos mover un vagon
    # si no está previamente desacoplado o la composicion a la que pertenece está en destino.
    if vagon.composicion == None or vagon.composicion_posicionada(destino):
        # Movemos el vagon a nuevo lugar
        vagon.mover(destino)
        # extraemos los bogies y los ejes de la composición y los movemos
        bogies = Bogie.objects.filter(vagon = vagon)
        ejes = Eje.objects.filter(vagon = vagon)
        for bogie in bogies:
            bogie.mover(destino)
        for eje in ejes:
            eje.mover(destino)

def mover_composicion(composicion, destino):
    # Movemos la composición a nuevo lugar
    composicion.mover(destino)
    # extraemos los vagones de la composición y los movemos
    vagones = Vagon.objects.filter(composicion = composicion)
    for vagon in vagones:
        mover_vagon(vagon, destino)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Funciones para componer y descomponer composiciones, vagones y bogies
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# funciones de destrucción
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def desacoplar_bogie(bogie):
    # desasociamos el bogie del vagón al que perteneciera
    bogie.desacoplar_de_vagon()
    # desasociamos tambien los ejes que van en el bogie del vagón
    # los vagones pueden ser con bogies y con ejes. Por eso los ejes van referenciados al bogie y
    # al vagón en el que van. Al sacar el bogie del vagon no hay que olvidar sacar también los ejes
    ejes = Eje.objects.filter(bogie = bogie)
    for eje in ejes:
        eje.desacoplar_de_vagon()

def deshacer_bogie(bogie):
    # Comprobamos que el bogie no esté acoplado a ningún vagón
    # si lo estuviera primero habria que desacoplarlo y luego podemos deshacerlo
    if bogie.vagon == None:
        # desasociamos los ejes del bogie
        ejes = Eje.objects.filter(bogie = bogie)
        for eje in ejes:
            eje.desacoplar_de_bogie()

def desacoplar_vagon(vagon):
    # Desasociamos el vagon de la composición a la que perteneciera.
    # ... como ayuda: solo cuando el vagón queda suelto podrá moverse por separado (funcion mover_vagon())
    vagon.desacoplar_de_composicion()

def deshacer_vagon(vagon):
    # Comprobamos que el vagón no esté acoplado a ningúna composición
    # si lo estuviera primero habria que desacoplarlo y luego podemos deshacerlo
    if vagon.composicion == None:
        # desasociamos los bogies del vagón
        bogies = Bogie.objects.filter(vagon = vagon)
        for bogie in bogies:
            desacoplar_bogie(bogie)
        # En caso de que quede algún eje asociado al vagón (vagones de ejes), los desacoplamos.
        ejes = Eje.objects.filter(vagon = vagon)
        for eje in ejes:
            eje.desacoplar_de_vagon()

def deshacer_composicion(composicion):
    # desacoplamos todos los vagones de la composición
    vagones = Vagon.objects.filter(composicion = composicion)
    for vagon in vagones:
        desacoplar_vagon(vagon)
    # luego eliminamos la composición.
    composicion.delete()

def quitar_a_composicion(composicion, lista_vagones):
    vagones = Vagon.objects.filter(codigo__in = lista_vagones)
    for vagon in vagones:
        if vagon.composicion == composicion:
            desacoplar_vagon(vagon)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# funciones de construcción
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def formar_bogie(bogie, lista_ejes):
    # Función para componer bogie con nuevos ejes
    ejes = Eje.objects.filter(codigo__in=lista_ejes)
    destino = {'lng': bogie.lng, 'lat': bogie.lat}
    for eje in ejes:
        eje.acoplar_a_bogie(bogie)
        eje.acoplar_a_vagon(bogie.vagon)
        eje.mover(destino)

def formar_vagon(vagon, lista_bogies=[], lista_ejes = []):
    # Función para componer un vagón con nuevos bogies y nuevos ejes
    # primero los bogies y los ejes asociados a esos ejes
    destino = {'lng': vagon.lng, 'lat': vagon.lat}
    if len(lista_bogies) > 0:
        bogies = Bogie.objects.filter(codigo__in = lista_bogies)
        for bogie in bogies:
            bogie.acoplar_a_vagon(vagon)
            bogie.mover(destino)
            ejes = Eje.objects.filter(bogie = bogie)
            for eje in ejes:
                eje.acoplar_a_vagon(vagon)
                eje.mover(destino)
    # despues los ejes de la lista pasada (esto representa los vagones que no tienen bogies y los ejes van directamente al vagón)
    if len(lista_ejes) > 0:
        ejes = Eje.objects.filter(codigo__in = lista_ejes)
        for eje in ejes:
            eje.acoplar_a_vagon(vagon)
            eje.mover(destino)

def formar_composicion(data_composicion, posicion, lista_vagones):
    composicion = Composicion(codigo = data_composicion['codigo'], descripcion = data_composicion['descripcion'])
    composicion.save()
    try:
        operador = Operador.objects.get(organizacion__codigo = data_composicion['operador'])
        composicion.operador = operador
        composicion.lng = posicion['lng']
        composicion.lat = posicion['lat']
        vagones = Vagon.objects.filter(codigo__in = lista_vagones)
        for vagon in vagones:
            mover_vagon(vagon, posicion)
            vagon.acoplar_a_composicion(composicion)
    finally:
        composicion.save()
    
def añadir_a_composicion(composicion, lista_vagones):
    destino = {'lng': composicion.lng, 'lat': composicion.lat}
    vagones = Vagon.objects.filter(codigo__in = lista_vagones)
    for vagon in vagones:
        mover_vagon(vagon, destino)
        vagon.acoplar_a_composicion(composicion)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# funciones de registro de circualciones
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def registrar_circulacion_composicion(composicion, circulacion):
    pass