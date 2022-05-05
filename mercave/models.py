from django.db import models
from django.urls import reverse

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

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Elementos del sistema Mercave
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Composicion(models.Model):
    codigo = models.CharField(max_length=16, unique= True)
    descripcion = models.CharField(max_length=100, default = ' ')
    operador= models.ForeignKey(Operador, on_delete=models.CASCADE)
    lng = models.FloatField(default=-3.9820) # grados
    lat = models.FloatField(default=40.2951) # grados

    def __str__(self):
        return self.codigo
    def get_absolute_url(self):
        return reverse("ficha_tren", kwargs={'pk':self.pk})

class Vagon(models.Model):
    codigo = models.CharField(max_length=16, unique= True)
    tipo = models.CharField(max_length=20,default = ' ')
    descripcion = models.CharField(max_length=100, default = ' ')
    foto = models.ImageField(upload_to='vagones/', blank = True)
    operador= models.ForeignKey(Operador, on_delete=models.RESTRICT)
    keeper= models.ForeignKey(Keeper, on_delete=models.RESTRICT)
    mantenedor= models.ForeignKey(Mantenedor, on_delete=models.RESTRICT, limit_choices_to={'de_vagones': True},)
    composicion= models.ForeignKey(Composicion, on_delete=models.RESTRICT)
    lng = models.FloatField(default=-3.9820) # grados
    lat = models.FloatField(default=40.2951) # grados

    def __str__(self):
        return self.codigo
    def get_absolute_url(self):
        return reverse("ficha_vagon", kwargs={'pk':self.pk})

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
            
class Eje(models.Model):
    codigo = models.CharField(max_length=10, unique= True)
    version= models.ForeignKey(VersionEje, on_delete=models.RESTRICT)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.RESTRICT, limit_choices_to={'de_ejes': True},)
    keeper = models.ForeignKey(Keeper, on_delete=models.RESTRICT)
    operador = models.ForeignKey(Operador, on_delete=models.RESTRICT)
    mantenedor = models.ForeignKey(Mantenedor, on_delete=models.RESTRICT)
    fecha_fab = models.DateField(auto_now_add=True)
    num_cambios = models.IntegerField(default=0)
    km = models.FloatField(default=0)                       # km
    mantenimiento = models.CharField(max_length=16)
    coef_trabajo = models.FloatField(default=0)
    vagon = models.ForeignKey(Vagon, on_delete=models.RESTRICT)
    alarmas_cambio = models.IntegerField(default=0)
    alarmas_circulacion = models.IntegerField(default=0)
    lng = models.FloatField(default=-3.9820)
    lat = models.FloatField(default=40.2951)

    def __str__(self):
        return self.codigo
    def get_absolute_url(self):
        return reverse("ficha_eje", kwargs={'pk':self.pk})

class VersionCambiador(models.Model):
    codigo= models.CharField(max_length=16, unique= True)
    opciones_anchos =  [('UIC-IB', 'UIC(1435) <> IBÉRICO (1668)'),
                        ('UIC-RUS', 'UIC(1435) <> RUSO (1520)'),
                        ('METR-UIC', 'MÉTRICO(1000) <> UIC(1435)'),]
    anchos = models.CharField(max_length=12, choices = opciones_anchos, default = 'UIC-IB')
    diseñador = models.ForeignKey(Diseñador, on_delete=models.RESTRICT, limit_choices_to={'de_cambiadores': True},)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.RESTRICT, limit_choices_to={'de_cambiadores': True},)
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
# Eventos
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
    linea = models.ForeignKey(Linea, on_delete=models.RESTRICT)
    pkilometrico = models.FloatField(null= True, blank = True)
    lng = models.FloatField(default=-3.9820)
    lat = models.FloatField(default=40.2951)
    def __str__(self):
        return (self.codigo)

class Inicio(models.Model):
    codigo = models.ForeignKey(PuntoRed, on_delete=models.CASCADE)
    def __str__(self):
        return (self.codigo)

class Final(models.Model):
    codigo = models.ForeignKey(PuntoRed, on_delete=models.CASCADE)
    def __str__(self):
        return (self.codigo)

class Circulacion(models.Model):
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
        return reverse("ficha_circulacion", kwargs={'pk':self.pk})
    
class AlarmaCambio(models.Model):
    cambio = models.ForeignKey(Cambio, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=30)
    vista = models.BooleanField(default=False)

    def __str__(self):
        return (self.mensaje)
    def get_absolute_url(self):
        return reverse("alarma_cambio", kwargs={'pk':self.pk})
    
class AlarmaCirculacion(models.Model):
    circulacion = models.ForeignKey(Circulacion, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    mensaje = models.CharField(max_length=30)
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
