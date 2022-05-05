import folium
from folium.plugins import MarkerCluster
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

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

def mapa_eje(eje):
    mapa_int = folium.Map((eje.lat, eje.lng), zoom_start=8)
    location = [eje.lat, eje.lng]
    html =  '<h5><b>EJE número: </b></h5>' + str(eje.codigo) +\
            '<br><b>Versión: </b>' + str(eje.version) +\
            '<br><b>Fabricante: </b>' + str(eje.fabricante) +\
            '<br><b>Num. Cambios: </b>' + str(eje.num_cambios) +\
            '<br><b>Kilómetros: </b>' + str(eje.km)

    popup = folium.Popup(html = html, max_width=150)
    marker = folium.Marker(location = location, popup = popup, icon = folium.Icon(color="red"))
    mapa_int.add_child(marker)    

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

def PloteaAlarmaCirc():
    x = list(range(10))
    ax = [-1.2,-0.3,4.5,5.3,1.4,-3.6,-5.9,0,2.2,1.1]
    ay = [2,5,0,-2,-5,-2,0,2,5,2]
    az = [-3,-1,2,9,1,-13,-5,0,3,0]
    p = figure(title="Aceleraciones", x_axis_label='x', y_axis_label='m/s^2')
    p.line(x, ax, legend_label="ax", line_width=2)
    p.line(x, ay, legend_label="ay", color="blue", line_width=2)
    p.line(x, az, legend_label="az", color="red", line_width=2)   

    return file_html(p, CDN, "Alarma Circulación")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def posicion(lugar):
    ''' 
    Función que devuelve la posición de un lugar conocido
    Argumentos:
        posicion: cadena con el nombre de la posición
    Devuelve:
        coordenadas: coordenadas de la posición solicitada. Si no se encuentra se devuelve la posición de TRIA
    '''
    lugar = lugar.upper()
    Tria = ['TRIA','NAVALCARNERO']
    Alcazar = ['ALCAZAR','ALCAZAR DE SAN JUÁN','ALCAZAR DE SAN JUAN']
    Miranda = ['MIRANDA','MIRANDA DE EBRO']
    Venta = ['VENTA DE BAÑOS','VENTA']
    Gabaldon = ['GABALDÓN','GABALDÓN','GABALDON']
    Calatayud = ['CALATAYUD']
    Aranjuez = ['ARANJUEZ']
    Leon = ['LEÓN','LEON']
    Tarragona = ['TARRAGONA']
    Zaragoza = ['ZARAGOZA']       
        
    if lugar in Tria:
        coordenadas = [-3.9820,40.2951]
    elif lugar in Alcazar:
        coordenadas = [-3.2138,39.4041]
    elif lugar in Miranda:
        coordenadas = [-2.9395,42.6919]
    elif lugar in Venta:
        coordenadas = [-4.5044,41.9110]
    elif lugar in Gabaldon:
        coordenadas = [-1.9472,39.6350]
    elif lugar in Calatayud:
        coordenadas = [-1.6358,41.3481]
    elif lugar in Aranjuez:
        coordenadas = [-3.5970,40.0159]
    elif lugar in Leon:
        coordenadas =[-5.5801,42.5772]
    elif lugar in Tarragona:
        coordenadas = [1.2053,41.0982]
    elif lugar in Zaragoza:
        coordenadas = [-0.7883,41.5892]
    else:
        coordenadas = [-3.9820,40.2951]
        print ('Todavía no hemos incorporado: ' + lugar + ' en la base de datos. Contacta con administrador')
        print ('Hemos mandado el Tren a TRIA para que le den un repaso')
        
    return coordenadas[0], coordenadas[1]