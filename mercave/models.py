from django.db import models
from django.urls import reverse
from pyparsing import null_debug_action

# Create your models here.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Actores del sistema Mercave
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Organizacion(models.Model):
    ''' Corresponde a la tabla de la base de datos con los datos de las organizaciones
        que participan en el ecosistema Mercave'''
    codigo = models.CharField(max_length=16,unique= True)
    nombre = models.CharField(max_length=50)
    cif = models.CharField(max_length=16)
    logo = models.CharField(max_length=150)
    color_corporativo = models.CharField(max_length=7)
    def __str__(self):
        return self.codigo
    def get_absolute_url(self):
        return reverse("ficha_organizacion", kwargs={'pk':self.pk})

class Diseñador(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    de_ejes = models.BooleanField(default=False)
    de_cambiadores = models.BooleanField(default=False)
    def __str__(self):
        return self.organizacion.codigo
    def get_absolute_url(self):
        return reverse("ficha_diseñador", kwargs={'pk':self.pk})

class Fabricante(models.Model):
    ''' hay campos para determinar las especializaciones del fabricante'''
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    de_ejes = models.BooleanField(default=False)
    de_cambiadores = models.BooleanField(default=False)
    de_bogies = models.BooleanField(default=False)
    de_vagones = models.BooleanField(default=False)
    def __str__(self):
        return self.organizacion.codigo
    def get_absolute_url(self):
        return reverse("ficha_fabricante", kwargs={'pk':self.pk})

class Mantenedor(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    de_ejes = models.BooleanField(default=False)
    de_cambiadores = models.BooleanField(default=False)
    de_bogies = models.BooleanField(default=False)
    de_vagones = models.BooleanField(default=False)
    def __str__(self):
        return self.organizacion.codigo
    def get_absolute_url(self):
        return reverse("ficha_mantenedor", kwargs={'pk':self.pk})

class Keeper(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    def __str__(self):
        return self.organizacion.codigo
    def get_absolute_url(self):
        return reverse("ficha_keeper", kwargs={'pk':self.pk})

class Operador(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    def __str__(self):
        return self.organizacion.codigo
    def get_absolute_url(self):
        return reverse("ficha_operador", kwargs={'pk':self.pk})

class Aprovador(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    def __str__(self):
        return self.organizacion.codigo
    def get_absolute_url(self):
        return reverse("ficha_aprovador", kwargs={'pk':self.pk})

class Certificador(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    def __str__(self):
        return self.organizacion.codigo
    def get_absolute_url(self):
        return reverse("ficha_certificador", kwargs={'pk':self.pk})
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Modelos que representan la ingeniería de los elementos mercave / Activos inmateriales
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class VersionEje(models.Model):
    codigo= models.CharField(max_length=16, unique= True)
    opciones_anchos =  [('UIC-IB', 'UIC(1435) <> IBÉRICO (1668)'),
                        ('UIC-RUS', 'UIC(1435) <> RUSO (1520)'),
                        ('UIC-RUS-IB', 'UIC <> RUSO <> IBÉRICO'),
                        ('METR-UIC', 'MÉTRICO(1000) <> UIC(1435)'),]
    anchos = models.CharField(max_length=12, choices = opciones_anchos, default = 'UIC-IB')
    diseñador = models.ForeignKey(Diseñador, on_delete=models.RESTRICT, limit_choices_to={'de_ejes': True},)
    rueda = models.CharField(max_length=16)
    cuerpo_eje = models.CharField(max_length=16)
    aprovador = models.ForeignKey(Aprovador, on_delete=models.RESTRICT)
    fecha_aprovacion = models.DateField()
    certificador = models.ForeignKey(Certificador, on_delete=models.RESTRICT)
    fecha_certificacion = models.DateField()
    def __str__(self):
        return self.codigo
    def get_absolute_url(self):
        return reverse("ficha_version_eje", kwargs={'pk':self.pk})

class VersionCambiador(models.Model):
    codigo= models.CharField(max_length=16, unique= True)
    opciones_anchos =  [('UIC-IB', 'UIC(1435) <> IBÉRICO (1668)'),
                        ('UIC-RUS', 'UIC(1435) <> RUSO (1520)'),
                        ('METR-UIC', 'MÉTRICO(1000) <> UIC(1435)'),]
    anchos = models.CharField(max_length=12, choices = opciones_anchos, default = 'UIC-IB')
    diseñador = models.ForeignKey(Diseñador, on_delete=models.RESTRICT, limit_choices_to={'de_cambiadores': True},)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.RESTRICT, limit_choices_to={'de_cambiadores': True}, null=True, blank=True)
    longitud_desencerrojado = models.FloatField(default=6000)   # mm
    longitud_cambio_rueda = models.FloatField(default=6000)     # mm
    longitud_encerrojado = models.FloatField(default=6000)      # mm
    longitud_total = models.FloatField(default = 36000)         # mm
    aprovador = models.ForeignKey(Aprovador, on_delete=models.RESTRICT)
    fecha_aprovacion = models.DateField()
    certificador = models.ForeignKey(Certificador, on_delete=models.RESTRICT)
    fecha_certificacion = models.DateField()
    def __str__(self):
        return self.codigo
    def get_absolute_url(self):
        return reverse("ficha_version_cambiador", kwargs={'pk':self.pk})
            

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Elementos del sistema Mercave / Activos físicos
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Aquí hay algo de locura. Las composiciones tienen vagones y estos a veces tienen bogies
# que llevan ejes y a veces no llevan bogies y los ejes van directamente a los vagones.
# la estructura de datos es flexible y se supone que las funciones que tengan que formar 
# composiciones, vagones, etc se encargarán e mantener todo coherentemente. ahora un eje 
# podría quedar asignado a un bogie y a un vagón que no van juntos.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Composicion(models.Model):
    codigo = models.CharField(max_length=16, unique= True)
    descripcion = models.CharField(max_length=100, default = ' ')
    operador= models.ForeignKey(Operador, on_delete=models.CASCADE, null=True, blank=True)
    lng = models.FloatField(default=-3.9820) # grados
    lat = models.FloatField(default=40.2951) # grados
    def __str__(self):
        return self.codigo
    def get_absolute_url(self):
        return reverse("ficha_composicion", kwargs={'pk':self.pk})
    def mover(self, localizacion):
        self.lng = localizacion['lng']
        self.lat = localizacion['lat']
        self.save()

class Vagon(models.Model):
    codigo = models.CharField(max_length=16, unique= True)
    tipo = models.CharField(max_length=20,default = ' ')
    descripcion = models.CharField(max_length=100, default = ' ')
    num_bogies= models.IntegerField(default=2, null=True, blank=True)
    num_ejes = models.IntegerField(default=4, null=True, blank=True)
    foto = models.ImageField(upload_to='vagones/', blank = True)
    operador= models.ForeignKey(Operador, on_delete=models.RESTRICT, null=True, blank=True)
    keeper= models.ForeignKey(Keeper, on_delete=models.RESTRICT, null=True, blank=True)
    mantenedor= models.ForeignKey(Mantenedor, on_delete=models.RESTRICT, limit_choices_to={'de_vagones': True}, null=True, blank=True)
    composicion= models.ForeignKey(Composicion, on_delete=models.RESTRICT, null=True, blank=True)
    lng = models.FloatField(default=-3.9820) # grados
    lat = models.FloatField(default=40.2951) # grados
    def __str__(self):
        return self.codigo
    def get_absolute_url(self):
        return reverse("ficha_vagon", kwargs={'pk':self.pk})
    # Funciones creadas para leer y guardar datos de las lógicas de negocio de logistica_feroviaria
    def composicion_posicionada(self, posicion):
        if self.composicion:
            if (self.composicion.lng == posicion['lng'] and self.composicion.lat == posicion['lat']):
                return True
            else:
                return False
        return True
    def mover(self, posicion):
        self.lng = posicion['lng']
        self.lat = posicion['lat']
        self.save()
    def desacoplar_de_composicion(self):
        self.composicion = None
        self.save()
    def acoplar_a_composicion(self, composicion):
        self.composicion = composicion
        self.save()

class Bogie(models.Model):
    codigo = models.CharField(max_length=16, unique= True)
    tipo = models.CharField(max_length=20,default = ' ')
    foto = models.ImageField(upload_to='bogies/', blank = True)
    operador= models.ForeignKey(Operador, on_delete=models.RESTRICT, null=True, blank=True)
    keeper= models.ForeignKey(Keeper, on_delete=models.RESTRICT, null=True, blank=True)
    mantenedor= models.ForeignKey(Mantenedor, on_delete=models.RESTRICT, limit_choices_to={'de_bogies': True},)
    vagon= models.ForeignKey(Vagon, on_delete=models.RESTRICT, null=True, blank=True)
    lng = models.FloatField(default=-3.9820) # grados
    lat = models.FloatField(default=40.2951) # grados
    def __str__(self):
        return self.codigo
    def get_absolute_url(self):
        return reverse("ficha_bogie", kwargs={'pk':self.pk})
    def mover(self, localizacion):
        self.lng = localizacion['lng']
        self.lat = localizacion['lat']
        self.save()
    def desacoplar_de_vagon(self):
        self.vagon = None
        self.save()
    def acoplar_a_vagon(self, vagon):
        self.vagon = vagon
        self.save()

class Eje(models.Model):
    codigo = models.CharField(max_length=10, unique= True)
    version= models.ForeignKey(VersionEje, on_delete=models.RESTRICT)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.RESTRICT, limit_choices_to={'de_ejes': True},)
    keeper = models.ForeignKey(Keeper, on_delete=models.RESTRICT)
    operador = models.ForeignKey(Operador, on_delete=models.RESTRICT)
    mantenedor = models.ForeignKey(Mantenedor, on_delete=models.RESTRICT)
    fecha_fab = models.DateField(auto_now_add=True)
    num_cambios = models.IntegerField(default=0)
    km = models.FloatField(default=0)         # km
    mantenimiento = models.CharField(max_length=16, null=True, blank=True)
    coef_trabajo = models.FloatField(default=0)
    bogie = models.ForeignKey(Bogie, on_delete=models.RESTRICT, null=True, blank=True)
    vagon = models.ForeignKey(Vagon, on_delete=models.RESTRICT, null=True, blank=True)
    alarmas = models.IntegerField(default=0, null=True, blank=True)
    lng = models.FloatField(default=-3.9820)
    lat = models.FloatField(default=40.2951)
    def __str__(self):
        return self.codigo
    def get_absolute_url(self):
        return reverse("ficha_eje", kwargs={'pk':self.pk})
    def mover(self, localizacion):
        self.lng = localizacion['lng']
        self.lat = localizacion['lat']
        self.save()
    def desacoplar_de_bogie(self):
        self.bogie = None
        self.save()
    def desacoplar_de_vagon(self):
        self.vagon = None
        self.save()
    def acoplar_a_bogie(self, bogie):
        self.bogie = bogie
        self.save()
    def acoplar_a_vagon(self, vagon):
        self.vagon = vagon
        self.save()


class Cambiador(models.Model):
    codigo = models.CharField(max_length=16, unique= True)
    nombre = models.CharField(max_length=100, default = 'Experimental-01')
    version= models.ForeignKey(VersionCambiador, on_delete=models.RESTRICT)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.RESTRICT, limit_choices_to={'de_cambiadores': True},)
    mantenedor = models.ForeignKey(Mantenedor, on_delete=models.RESTRICT, limit_choices_to={'de_cambiadores': True},)
    fecha_fab = models.DateField(auto_now_add=True)
    num_cambios = models.IntegerField(default=0)
    mantenimiento = models.CharField(max_length=16)
    lng = models.FloatField(default=-4.6920) # grados
    lat = models.FloatField(default=37.9246) # grados

    def __str__(self):
        return (str(self.codigo) + ': ' + str(self.nombre))
    def get_absolute_url(self):
        return reverse("ficha_cambiador", kwargs={'pk':self.pk})

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Modelos que identifican puntos singulares de la red ferroviaria
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Linea(models.Model):
    codigo = models.CharField(max_length=16, unique= True)
    nombre = models.CharField(max_length=100, null= True, blank = True)
    def __str__(self):
        return (str(self.codigo) + '-' + str(self.nombre))
    def get_absolute_url(self):
        return reverse("ficha_linea", kwargs={'pk':self.pk})

class PuntoRed(models.Model):
    codigo = models.CharField(max_length=16, unique= True)
    descripcion = models.CharField(max_length=100, null= True, blank = True)
    linea = models.ForeignKey(Linea, on_delete=models.RESTRICT, null= True, blank = True)
    pkilometrico = models.FloatField(null= True, blank = True)
    lng = models.FloatField(default=-3.9820)
    lat = models.FloatField(default=40.2951)
    def __str__(self):
        return (self.codigo)

# Inicio y final son para poder referenciar 2 puntos de red dentro de una msma circulación
class Inicio(models.Model):
    puntored = models.ForeignKey(PuntoRed, on_delete=models.CASCADE)
    def __str__(self):
        return (self.puntored.codigo)
        
class Final(models.Model):
    puntored = models.ForeignKey(PuntoRed, on_delete=models.CASCADE)
    def __str__(self):
        return (self.puntored.codigo)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# EVENTOS. Llegan desde API de mercave_accion (IoT, IA).
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Cambio(models.Model):
    eje = models.ForeignKey(Eje, on_delete=models.CASCADE)
    num_cambio_eje = models.IntegerField(default=0)
    alarma = models.BooleanField(default=False)
    inicio = models.DateTimeField()
    cambiador = models.ForeignKey(Cambiador, on_delete=models.RESTRICT)
    opciones_sentido =  [('UICIB', 'UIC->IB'),
                         ('IBUIC', 'IB->UIC'),
                         ('UICRUS', 'UIC->RUS'),
                         ('RUSUIC', 'RUS->UIC')]
    sentido = models.CharField(max_length=8, choices = opciones_sentido, default = 'UICIB')                 
    V = models.FloatField(default = 2.77)       # Velocidad de entrada m/s
    FV = models.FloatField(default = 250)       # Fuerza Vertical (peso en eje) KN
    # VALORES RUEDA A
    tdaM = models.FloatField(default = 5000)  # tiempo (ms) desde inicio punto de F máxima en desencerrojamiento
    fdaM = models.FloatField(default = 30)    # fuerza (KN) máxima en desencerrojamiento
    ddaM = models.FloatField(default = 10)    # desplazamiento (mm) de disco en punto de f máxima en desencerrojamiento
    tcaM = models.FloatField(default = 10000)  # tiempo (ms) desde inicio punto de F máxima en cambio
    fcaM = models.FloatField(default = 20)    # fuerza (KN) máxima en desencerrojamiento
    dcaM = models.FloatField(default = 70)  # desplazamiento (mm) de rueda en punto de F máxima en cambio
    team = models.FloatField(default = 15000)  # tiempo (ms) desde inicio punto de F minima en encerrojamiento
    feam = models.FloatField(default = 10)    # fuerza (KN) mínima en encerrojamiento
    deam = models.FloatField(default = 20)  # desplazamiento (mm) de disco en punto de F mínima en encerrojamiento
    # VALORES RUEDA B 
    tdbM = models.FloatField(default = 25000)  # tiempo (ms) desde inicio punto de F máxima en desencerrojamiento
    fdbM = models.FloatField(default = 30)    # fuerza (KN) máxima en desencerrojamiento
    ddbM = models.FloatField(default = 10)    # desplazamiento (mm) de disco en punto de f máxima en desencerrojamiento
    tcbM = models.FloatField(default = 300000)  # tiempo (ms) desde inicio punto de F máxima en cambio
    fcbM = models.FloatField(default = 20)    # fuerza (KN) máxima en desencerrojamiento
    dcbM = models.FloatField(default = 70)  # desplazamiento (mm) de rueda en punto de F máxima en cambio
    tebm = models.FloatField(default = 35000)  # tiempo (ms) desde inicio punto de F minima en encerrojamiento
    febm = models.FloatField(default = 10)    # fuerza (KN) mínima en encerrojamiento
    debm = models.FloatField(default = 20)  # desplazamiento (mm) de disco en punto de F mínima en encerrojamiento
    def __str__(self):
        return (str(self.inicio) + '-' + str(self.cambiador.nombre) + '- eje: ' + str(self.eje.codigo))
    def get_absolute_url(self):
        return reverse("ficha_cambio", kwargs={'pk':self.pk})

# definimos 3 circulaciones aunque con 1 (composicion) debería bastar. De momento nos simplifica un poco
# la vida a la hora de mostrar las circulaciones de un eje.
class CirculacionComposicion(models.Model):
    composicion = models.ForeignKey(Composicion, on_delete=models.CASCADE)
    pinicio = models.ForeignKey(Inicio, on_delete=models.RESTRICT, null= True, blank = True)
    pfinal = models.ForeignKey(Final, on_delete=models.RESTRICT, null= True, blank = True)
    dia = models.DateField()
    Vmed = models.FloatField(default = 2.77)
    km = models.FloatField(default = 340)
    alarmas = models.BooleanField(default=False)
    def __str__(self):
        return (str(self.composicion.codigo) + '-' + str(self.dia))
    def get_absolute_url(self):
        return reverse("ficha_circulacion_composicion", kwargs={'pk':self.pk})

class CirculacionVagon(models.Model):
    vagon = models.ForeignKey(Vagon, on_delete=models.CASCADE)
    pinicio = models.ForeignKey(Inicio, on_delete=models.RESTRICT, null= True, blank = True)
    pfinal = models.ForeignKey(Final, on_delete=models.RESTRICT, null= True, blank = True)
    dia = models.DateField()
    Vmed = models.FloatField(default = 2.77)
    km = models.FloatField(default = 340)
    alarmas = models.BooleanField(default=False)
    def __str__(self):
        return (str(self.vagon.codigo) + '-' + str(self.dia))
    def get_absolute_url(self):
        return reverse("ficha_circulacion_vagon", kwargs={'pk':self.pk})

class CirculacionEje(models.Model):
    eje = models.ForeignKey(Eje, on_delete=models.CASCADE)
    pinicio = models.ForeignKey(Inicio, on_delete=models.RESTRICT, null= True, blank = True)
    pfinal = models.ForeignKey(Final, on_delete=models.RESTRICT, null= True, blank = True)
    dia = models.DateField()
    Vmed = models.FloatField(default = 2.77)
    km = models.FloatField(default = 340)
    alarmas = models.BooleanField(default=False)
    def __str__(self):
        return (str(self.eje.codigo) + '-' + str(self.dia))
    def get_absolute_url(self):
        return reverse("ficha_circulacion_eje", kwargs={'pk':self.pk})

# PuntoTransito son eventos singulares en puntos de la red en un instante determinado donde
# se ha producido una alarma u otro evento destacable. Se asocia a una circulación de un eje concreto
class PuntoTransito(models.Model):
    fecha_hora = fecha_hora = models.DateTimeField(auto_now_add=True)
    punto_red  = models.ForeignKey(PuntoRed, on_delete=models.CASCADE, null= True, blank = True)
    circulacion = models.ForeignKey(CirculacionEje, on_delete=models.CASCADE, null= True, blank = True)
    def __str__(self):
        return (str(self.fecha_hora) + '-' + str(self.eje.punto))


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class AlarmaCambio(models.Model):
    cambio = models.ForeignKey(Cambio, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=30)
    vista = models.BooleanField(default=False)
    def __str__(self):
        return (self.mensaje)
    def get_absolute_url(self):
        return reverse("alarma_cambio", kwargs={'pk':self.pk})
    
class AlarmaCirculacion(models.Model):
    circulacion = models.ForeignKey(CirculacionEje, on_delete=models.CASCADE, null= True, blank = True)
    punto_transito = models.ForeignKey(PuntoTransito, on_delete=models.CASCADE, null= True, blank = True)
    fecha_hora = models.DateTimeField()
    mensaje = models.CharField(max_length=30)
    lng = models.FloatField(default=-3.9820, null= True, blank = True)
    lat = models.FloatField(default=40.2951, null= True, blank = True)
    vista = models.BooleanField(default=False)
    ax0 = models.FloatField(default = 2.77)
    ay0 = models.FloatField(default = 2.77)
    az0 = models.FloatField(default = 2.77)
    t0 = models.FloatField(default = 2.77)
    ax1 = models.FloatField(default = 2.77)
    ay1 = models.FloatField(default = 2.77)
    az1 = models.FloatField(default = 2.77)
    t1 = models.FloatField(default = 2.77)
    ax2 = models.FloatField(default = 2.77)
    ay2 = models.FloatField(default = 2.77)
    az2= models.FloatField(default = 2.77)
    t2 = models.FloatField(default = 2.77)  
    ax3 = models.FloatField(default = 2.77)
    ay3 = models.FloatField(default = 2.77)
    az3= models.FloatField(default = 2.77)
    t3 = models.FloatField(default = 2.77)  
    ax4 = models.FloatField(default = 2.77)
    ay4 = models.FloatField(default = 2.77)
    az4= models.FloatField(default = 2.77)
    t4 = models.FloatField(default = 2.77)  
    ax5 = models.FloatField(default = 2.77)
    ay5 = models.FloatField(default = 2.77)
    az5 = models.FloatField(default = 2.77)
    t5 = models.FloatField(default = 2.77)  
    ax6 = models.FloatField(default = 2.77)
    ay6 = models.FloatField(default = 2.77)
    az6 = models.FloatField(default = 2.77)
    t6 = models.FloatField(default = 2.77)  
    ax7 = models.FloatField(default = 2.77)
    ay7 = models.FloatField(default = 2.77)
    az7 = models.FloatField(default = 2.77)
    t7 = models.FloatField(default = 2.77)  
    ax8 = models.FloatField(default = 2.77)
    ay8 = models.FloatField(default = 2.77)
    az8 = models.FloatField(default = 2.77)
    t8 = models.FloatField(default = 2.77)  
    ax9 = models.FloatField(default = 2.77)
    ay9 = models.FloatField(default = 2.77)
    az9= models.FloatField(default = 2.77)
    t9 = models.FloatField(default = 2.77)  

    def __str__(self):
        return (self.mensaje)
    def get_absolute_url(self):
        return reverse("alarma_circulacion", kwargs={'pk':self.pk})
