import folium
from folium.plugins import MarkerCluster

def mapa_ejes(ejes):
    mapa = folium.Map((39.8000, -2.9019), zoom_start=6)
    mc = MarkerCluster()
    for eje in ejes:
        location = [eje.lat, eje.lng]
        html =  '<h5><b>EJE: <br><br>' + str(eje.codigo) + '</b></h5>' +\
                '<br><b>Bogie: </b>' + str(eje.bogie) +\
                '<br><b>Vagón: </b>' + str(eje.vagon) +\
                '<br><b>Versión: </b>' + str(eje.version) +\
                '<br><b>Fabricante: </b>' + str(eje.fabricante) +\
                '<br><b>Num. Cambios: </b>' + str(eje.num_cambios) +\
                '<br><b>Kilómetros: </b>' + str(eje.km)

        popup = folium.Popup(html = html, max_width=150)
        marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="red"))
        mc.add_child(marker)
    mapa.add_child(mc)    

    return mapa._repr_html_()

def mapa_eje(eje, circulaciones):
    mapa_int = folium.Map((eje.lat, eje.lng), zoom_start=6)
    colores = ['#E1E3F8','#AAB2F6','#7D89F7','#5363F8','#263AF8']
    # Pop up eje
    location = [eje.lat, eje.lng]
    html =  '<h5><b>EJE: <br><br>' + str(eje.codigo) + '</b></h5>' +\
                '<br><b>Bogie: </b>' + str(eje.bogie) +\
                '<br><b>Vagón: </b>' + str(eje.vagon) +\
                '<br><b>Versión: </b>' + str(eje.version) +\
                '<br><b>Fabricante: </b>' + str(eje.fabricante) +\
                '<br><b>Num. Cambios: </b>' + str(eje.num_cambios) +\
                '<br><b>Kilómetros: </b>' + str(eje.km)
    popup = folium.Popup(html = html, max_width=150)
    marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="red"))
    mapa_int.add_child(marker) 
    # Posiciones
    i= 0
    for circulacion in circulaciones:    
        location = [circulacion.pinicio.puntored.lat, circulacion.pinicio.puntored.lng]
        color = colores[i]
        popup = str(circulacion.pinicio.puntored.descripcion) + ' - ' + str(circulacion.dia)
        folium.CircleMarker(
            location = location,
            radius = 10,
            popup= popup,
            color=color,
            fill = True,
            fill_color = color,
        ).add_to(mapa_int)
        i += 1

    return mapa_int._repr_html_()

def mapa_cambiadores(cambiadores):
    mapa = folium.Map((39.8000, -2.9019), zoom_start=6)
    mc = MarkerCluster()
    
    for cambiador in cambiadores:    
        location = [cambiador.lat, cambiador.lng]
        html =  '<h6><b>CAMBIADOR DE ANCHO : </b>' + str(cambiador.nombre)+ '<h6>' +\
                '<br><b> Versión: </b>' + str(cambiador.version) +\
                '<br><b> Fabricante: </b>' + str(cambiador.fabricante) +\
                '<br><b> Puesta en servicio: </b>' + str(cambiador.fecha_fab) +\
                '<br><b> Número de operaciones: </b>' + str(cambiador.num_cambios)       
        popup = folium.Popup(html = html, max_width=200)
        marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="darkgreen", icon = 'plus'))
        mc.add_child(marker)
    mapa.add_child(mc)    

    return mapa._repr_html_()

def mapa_cambiador(cambiador):
    mapa = folium.Map((39.8000, -2.9019), zoom_start=6)
    mc = MarkerCluster()
     
    location = [cambiador.lat, cambiador.lng]
    html =  '<h6><b>CAMBIADOR DE ANCHO : </b>' + str(cambiador.nombre)+ '<h6>' +\
            '<br><b> Versión: </b>' + str(cambiador.version) +\
            '<br><b> Fabricante: </b>' + str(cambiador.fabricante) +\
            '<br><b> Puesta en servicio: </b>' + str(cambiador.fecha_fab) +\
            '<br><b> Número de operaciones: </b>' + str(cambiador.num_cambios)       
    popup = folium.Popup(html = html, max_width=200)
    marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="darkgreen", icon = 'plus'))
    mc.add_child(marker)
    mapa.add_child(mc)    

    return mapa._repr_html_()

def mapa_vagones(vagones):
    mapa = folium.Map((39.8000, -2.9019), zoom_start=6)
    mc = MarkerCluster()
    
    for vagon in vagones:    
        location = [vagon.lat, vagon.lng]
        html =  '<h6><b>VAGÓN : </b>' + str(vagon.codigo)+ '<h6>' +\
                '<br><b> Tipo:' + str(vagon.tipo) + '</b>' +\
                '<br><b> Descripción:' + str(vagon.descripcion) + '</b>' +\
                '<br><b> Operador: </b>' + str(vagon.operador)  
        popup = folium.Popup(html = html, max_width=200)
        marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="darkblue"))
        mc.add_child(marker)
    mapa.add_child(mc)    

    return mapa._repr_html_()

def mapa_vagon(vagon, circulaciones):
    mapa_int = folium.Map((vagon.lat, vagon.lng), zoom_start=6)
    # Pop up eje
    location = [vagon.lat, vagon.lng]
    html =  '<h6><b>VAGON : </b>' + str(vagon.codigo)+ '<h6>'  
    popup = folium.Popup(html = html, max_width=150)
    marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="darkblue"))
    mapa_int.add_child(marker) 

    return mapa_int._repr_html_()

def mapa_composiciones(composiciones):
    mapa = folium.Map((39.8000, -2.9019), zoom_start=6)
    mc = MarkerCluster()
    
    for composicion in composiciones:    
        location = [composicion.lat, composicion.lng]
        html =  '<h6><b>COMPOSICIÓN : </b>' + str(composicion.codigo)+ '<h6>' +\
                '<br><b>' + str(composicion.descripcion) + '</b>' +\
                '<br><b> Operador: </b>' + str(composicion.operador)  
        popup = folium.Popup(html = html, max_width=200)
        marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="purple", icon = 'c'))
        mc.add_child(marker)
    mapa.add_child(mc)    

    return mapa._repr_html_()

def mapa_composicion(composicion, circulaciones):
    mapa_int = folium.Map((composicion.lat, composicion.lng), zoom_start=6)
    # Pop up eje
    location = [composicion.lat, composicion.lng]
    html =  '<h6><b>COMPOSICIÓN : </b>' + str(composicion.codigo)+ '<h6>' +\
            '<br><b>' + str(composicion.descripcion) + '</b>' +\
            '<br><b> Operador: </b>' + str(composicion.operador)  
    popup = folium.Popup(html = html, max_width=150)
    marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="purple", icon = 'c'))
    mapa_int.add_child(marker) 

    # Posiciones
    for circulacion in circulaciones:    
        location = [circulacion.pinicio.puntored.lat, circulacion.pinicio.puntored.lng]
        color = 'cadetblue'
        popup = str(circulacion.pinicio.puntored.descripcion) + ' - ' + str(circulacion.dia)
        folium.CircleMarker(
            location = location,
            radius = 10,
            popup= popup,
            color=color,
            fill = True,
            fill_color = color,
        ).add_to(mapa_int)

    return mapa_int._repr_html_()
    
def mapa_cambios(cambios):
    mapa = folium.Map((39.8000, -2.9019), zoom_start=5)
    mc = MarkerCluster()
    
    for cambio in cambios:    
        location = [cambio.cambiador.lat, cambio.cambiador.lng]
        html =  '<b> Eje: </b>' + str(cambio.eje.codigo) +\
                '<br><b>Cambiador : </b>' + str(cambio.cambiador.nombre)+\
                '<br><b> fecha: </b>' + str(cambio.inicio) +\
                '<br><b> sentido: </b>' + str(cambio.sentido)  
        popup = folium.Popup(html = html, max_width=200)
        marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="blue"))
        mc.add_child(marker)
    mapa.add_child(mc)    

    return mapa._repr_html_()