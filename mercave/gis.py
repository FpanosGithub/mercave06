import folium
from folium.plugins import MarkerCluster
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.layouts import row
from bokeh.models import BoxAnnotation

def mapa_ejes(ejes):
    mapa = folium.Map((39.8000, -2.9019), zoom_start=6)
    mc = MarkerCluster()
    for eje in ejes:
        location = [eje.lat, eje.lng]
        html =  '<h5><b>EJE número: </b></h5>' + str(eje.codigo) +\
                '<br><b>Versión: </b>' + str(eje.version) +\
                '<br><b>Fabricante: </b>' + str(eje.fabricante) +\
                '<br><b>Num. Cambios: </b>' + str(eje.num_cambios) +\
                '<br><b>Kilómetros: </b>' + str(eje.km)

        popup = folium.Popup(html = html, max_width=150)
        marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="red"))
        mc.add_child(marker)
    mapa.add_child(mc)    

    return mapa._repr_html_()

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

def mapa_eje(eje, circulaciones):
    mapa_int = folium.Map((eje.lat, eje.lng), zoom_start=6)
    # Pop up eje
    location = [eje.lat, eje.lng]
    html =  '<h5><b>EJE número: </b></h5>' + str(eje.codigo) +\
            '<br><b>Versión: </b>' + str(eje.version) +\
            '<br><b>Fabricante: </b>' + str(eje.fabricante) +\
            '<br><b>Num. Cambios: </b>' + str(eje.num_cambios) +\
            '<br><b>Kilómetros: </b>' + str(eje.km)
    popup = folium.Popup(html = html, max_width=150)
    marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="red"))
    mapa_int.add_child(marker) 
    # Posiciones

    for circulacion in circulaciones:    
        location = [circulacion.pinicio.puntored.lat, circulacion.pinicio.puntored.lng]
        color = 'blue'
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

def plotear_alarma_circulacion():
    x = list(range(10))
    ax = [-1.2,-0.3,4.5,5.3,1.4,-3.6,-5.9,0,2.2,1.1]
    ay = [2,5,0,-2,-5,-2,0,2,5,2]
    az = [-3,-1,2,9,1,-13,-5,0,3,0]
    temp = [23,25,28,29,28,27,28,29,30, 31]
    mid_box_a = BoxAnnotation(bottom=-5, top=5, fill_alpha=0.2, fill_color="#009E73")
    mid_box_t = BoxAnnotation(bottom=25, top=40, fill_alpha=0.2, fill_color="#009E73")
    p1 = figure(title="Aceleraciones", x_axis_label='x',)
    p2 = figure(title="Temperatura", x_axis_label='x',)
    p1.line(x, ax, legend_label="ax m/s^2", line_width=2)
    p1.line(x, ay, legend_label="ay m/s^2", color="blue", line_width=2)
    p1.line(x, az, legend_label="az m/s^2", color="red", line_width=2)   
    p2.line(x, temp, legend_label="temp ºC", color="red", line_width=2)  
    p1.toolbar_location = None
    p2.toolbar_location = None
    p1.add_layout(mid_box_a)
    p2.add_layout(mid_box_t)
    r = row([p1, p2], sizing_mode="stretch_width")
    
    return file_html(r, CDN, "Alarma Circulación")

def plotear_cambios(cambios):
    fdM =[] 
    ddM =[]
    for cambio in cambios:
        fdM.append(cambio.fdaM)
        fdM.append(cambio.fdbM)
        ddM.append(cambio.ddaM)
        ddM.append(cambio.ddbM)

    p1 = figure(title="Fuerza Descerrojamiento", x_axis_label='mm de desplazamiento de disco',)
    p1.circle(ddM, fdM, legend_label="fd Kn", color="red", size=12)
    p1.toolbar_location = None
    
    return file_html(p1, CDN, "Cambios")