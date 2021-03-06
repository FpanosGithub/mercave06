from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.layouts import row
from bokeh.models import BoxAnnotation

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
    fcM =[] 
    dcM =[]
    fem =[] 
    dem =[]
    for cambio in cambios:
        fdM.append(cambio.fdaM)
        fdM.append(cambio.fdbM)
        ddM.append(cambio.ddaM)
        ddM.append(cambio.ddbM)
        fcM.append(cambio.fcaM)
        fcM.append(cambio.fcbM)
        dcM.append(cambio.dcaM)
        dcM.append(cambio.dcbM)
        fem.append(cambio.feam)
        fem.append(cambio.febm)
        dem.append(cambio.deam)
        dem.append(cambio.debm)

    p1 = figure(title="Fuerza Descerrojamiento", x_axis_label='mm de desplazamiento de disco',)
    p1.circle(ddM, fdM, legend_label="fd Kn", color="red", size=12)
    p1.toolbar_location = None
    
    p2 = figure(title="Fuerza Cambio Rueda", x_axis_label='mm de desplazamiento de rueda',)
    p2.circle(dcM, fcM, legend_label="fc Kn", color="green", size=12)
    p2.toolbar_location = None
    
    p3 = figure(title="Fuerza Encerrojamiento", x_axis_label='mm de desplazamiento de disco',)
    p3.circle(dem, fem, legend_label="fd Kn", color="blue", size=12)
    p3.toolbar_location = None
    
    # r = row([p1, p2, p3], sizing_mode="stretch_width")
    return file_html(p1, CDN, "Cambios"), file_html(p2, CDN, "Cambios"), file_html(p3, CDN, "Cambios")