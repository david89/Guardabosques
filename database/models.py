# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from datetime import date
from bitfield import BitField


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'


class Carrera(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    class Meta:
        db_table = u'carrera'
    def __unicode__(self):
        return self.nombre
        
class Usuario(models.Model):
    cedula = models.CharField(max_length=8, primary_key=True)
    carne = models.CharField(unique=True, max_length=8, default = None)
    clave = models.CharField(max_length=64)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.CharField(unique=True, max_length=50)
    telefono_principal = models.CharField(max_length=11)
    telefono_opcional = models.CharField(max_length=11)
    horas_laboradas = models.SmallIntegerField(default=0)
    horas_aprobadas = models.SmallIntegerField(default=0)
    estado = models.CharField(max_length=8)
    tipo = models.CharField(max_length=11)
    fecha_inicio = models.DateField(default = date.today())
    fecha_fin = models.DateField()
    zona = models.CharField(max_length=50)
    codigo_carrera = models.ForeignKey(Carrera, db_column='codigo_carrera')
    limitaciones_fisicas = models.TextField()
    limitaciones_medicas = models.TextField()
    class Meta:
        db_table = u'usuario'
    
    def inicializar(self):
        self.carne = None
        self.horas_laboradas = 0
        self.horas_aprobadas = 0
        self.fecha_inicio = date.today()

class Jornada(models.Model):
    id = models.AutoField(primary_key=True,db_column='identificador')
    cedula_usuario = models.ForeignKey(Usuario, db_column='cedula_usuario')
    fecha = models.CharField(max_length=10,blank=True)
    estado = models.CharField(max_length=9)
    minutos = models.SmallIntegerField()
    multiplicador = models.DecimalField(max_digits=4, decimal_places=1)
    class Meta:
        db_table = u'jornada'
        
class OtroServicio(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    class Meta:
        db_table = u'otro_servicio'

class Hizo(models.Model):
    identificador = models.AutoField(primary_key=True, )
    horas = models.SmallIntegerField()
    cedula_usuario = models.ForeignKey(Usuario, db_column='cedula_usuario')
    nombre_otro_servicio = models.ForeignKey(OtroServicio, db_column='nombre_otro_servicio')
    class Meta:
        db_table = u'hizo'

class Agrupacion(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    class Meta:
        db_table = u'agrupacion'

class Pertenece(models.Model):
    identificador = models.IntegerField(primary_key=True)
    cedula_usuario = models.ForeignKey(Usuario, db_column='cedula_usuario')
    nombre_agrupacion = models.ForeignKey(Agrupacion, db_column='nombre_agrupacion')
    class Meta:
        db_table = u'pertenece'

class Actividad(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    descripcion = models.TextField(blank=True)
    obj1 = models.BooleanField(blank=True)
    obj2 = models.BooleanField(blank=True)
    obj3 = models.BooleanField(blank=True)
    obj4 = models.BooleanField(blank=True)
    obj5 = models.BooleanField(blank=True)
    class Meta:
        db_table = u'actividad'
    def __unicode__(self):
        return self.nombre

class ConstituidaPor(models.Model):
    identificador = models.AutoField(primary_key=True)
    nombre_actividad = models.ForeignKey(Actividad, db_column='nombre_actividad')
    identificador_jornada = models.ForeignKey(Jornada, db_column='identificador_jornada')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    class Meta:
        db_table = u'constituida_por'