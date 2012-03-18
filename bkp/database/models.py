# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models

from datetime import date, datetime
from hashlib import sha256

USUARIO_ESTADOS = (
    (u'A', u'Activo'),
    (u'I', u'Inactivo'),
)
#
#USUARIO_TIPOS = (
#    (u'E', u'Estudiante'),
#    (u'C', u'Coordinador'),
#)
#
## NOTA: cedula, nombres, apellidos, clave y email en user.
###
##  Perfil que es creado por un coordinador.
#class PerfilPendiente(models.Model):
#    cedula = models.CharField(u'Cédula de identidad', max_length=8,
#                              unique=True)
#    correo = models.EmailField(u'Correo electrónico', unique=True)
#    tipo = models.CharField(choices=USUARIO_TIPOS, max_length=1)
#    estado = models.CharField(choices=USUARIO_ESTADOS, max_length=1)
#    verificador = models.CharField(max_length=64, editable=False, unique=True)
#    fecha_creacion = models.DateField(auto_now=True, editable=False)
#
#    def asunto_correo(self):
#        asunto = u'Sistema de Guardabosques: cuenta de usuario'
#
#        return asunto
#
#    def mensaje_correo(self, html=False):
#        mensaje = u'Esta es una invitación para el registro en el sistema '\
#                  u'de guardabosques de la USB. Si su cédula de identidad '\
#                  u'es %s por favor ingrese al siguiente enlace: %s. De lo '\
#                  u'contrario notifique al administrador del sistema acerca '\
#                  u'del error.'
#
#        enlace = "http://%s%s" % (settings.SITE_URL,
#                                  reverse(u'registro', args=[self.verificador]))
#
#        return mensaje % (self.cedula, enlace if not html else
#                                       u'<a href=%s>%s</a>' % (enlace, enlace))
#
#    def save(self, *args, **kwargs):
#        self.verificador = sha256(u'%s$%s' %
#                            (self.cedula, datetime.now())).hexdigest()
#
#        super(PerfilPendiente, self).save(*args, **kwargs)

##
#  Perfil de un usuario luego de que deja de ser pendiente y agrega sus datos.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, related_name=u'perfil')
    telefono_principal = models.CharField(max_length=11)
    telefono_opcional = models.CharField(blank=True, max_length=11, null=True)
    fecha_inicio = models.DateField(auto_now=True, editable=False)
    zona = models.CharField(max_length=50)

    def __unicode__(self):
        return self.usuario.username

##
#  Perfil que puede hacer labores administrativas en el sistema.
class Coordinador(Perfil):
    pass

##
#  Perfil que corresponde a un estudiante que realiza actividades y las
#  incorpora a una bitácora.
class Estudiante(Perfil):
    carne = models.CharField(max_length=8, unique=True)
    horas_laboradas = models.PositiveSmallIntegerField(default=0)
    horas_aprobadas = models.PositiveSmallIntegerField(default=0)
    estado = models.CharField(choices=USUARIO_ESTADOS, max_length=1)
    fecha_fin = models.DateField()
    limitaciones_fisicas = models.TextField(blank=True, null=True)
    limitaciones_medicas = models.TextField(blank=True, null=True)
    carrera = models.ForeignKey(u'Carrera')

    def __unicode__(self):
        return self.cedula

    def save(self, *args, **kwargs):
        if self.horas_aprobadas > self.horas_laboradas:
            raise ValidationError(u'El usuario no puede poseer más horas '\
                                  u'aprobadas que laboradas')

class Carrera(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)

    def __unicode__(self):
        return self.nombre

class Jornada(models.Model):
    id = models.AutoField(primary_key=True,db_column='identificador')
    #cedula_usuario = models.ForeignKey(Usuario, db_column='cedula_usuario')
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
    #cedula_usuario = models.ForeignKey(Usuario, db_column='cedula_usuario')
    nombre_otro_servicio = models.ForeignKey(OtroServicio, db_column='nombre_otro_servicio')
    class Meta:
        db_table = u'hizo'

class Agrupacion(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    class Meta:
        db_table = u'agrupacion'

class Pertenece(models.Model):
    identificador = models.IntegerField(primary_key=True)
    #cedula_usuario = models.ForeignKey(Usuario, db_column='cedula_usuario')
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
