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

USUARIO_TIPOS = (
    (u'E', u'Estudiante'),
    (u'C', u'Coordinador'),
)

# NOTA: cedula, nombres, apellidos, clave, estado y email en user.
##
#  Perfil que es creado por un coordinador.
class PerfilPendiente(models.Model):
    correo = models.EmailField(u'Correo electrónico', unique=True)
    activo = models.BooleanField(u'¿Usuario activo?')
    coordinador = models.BooleanField(u'¿Es coordinador?')
    verificador = models.CharField(max_length=64, editable=False, unique=True)
    fecha_creacion = models.DateField(auto_now=True, editable=False)

    ##
    #  Asunto para el correo a ser enviado en el correo relacionado con este
    #  perfil pendiente.
    def asunto_correo(self):
        asunto = u'Sistema de Guardabosques: cuenta de usuario'

        return asunto

    ##
    #  Mensaje para el correo a ser enviado en el correo relacionado con este
    #  perfil pendiente.
    def mensaje_correo(self, html=False):
        mensaje = u'Esta es una invitación para el registro en el sistema '\
                  u'de guardabosques de la USB. Por favor ingrese al '\
                  u'siguiente enlace: %s.'

        enlace = "http://%s%s" % (settings.SITE_URL,
                                  reverse(u'registrar_usuario',
                                          args=[self.verificador]))

        return mensaje % (enlace if not html else
                            u'<a href=%s>%s</a>' % (enlace, enlace))

    ##
    #  Operación guardar de la clase. El verificador se compone de la cédula
    #  de identidad del perfil pendiente junto con la fecha de creación del
    #  perfil pendiente.
    def save(self, *args, **kwargs):
        self.verificador = sha256(u'%s$%s' %
                            (self.correo, datetime.now())).hexdigest()

        super(PerfilPendiente, self).save(*args, **kwargs)

##
#  Perfil de un usuario luego de que deja de ser pendiente y agrega sus datos.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, related_name=u'perfil')
    carne = models.CharField(u'Carné', max_length=8, unique=True)
    telefono_principal = models.CharField(u'Teléfono principal',
                                          max_length=11)
    telefono_opcional = models.CharField(u'Teléfono opcional', blank=True,
                                         max_length=11, null=True)
    fecha_inicio = models.DateField(u'Fecha de inicio', auto_now_add=True,
                                    editable=False)
    zona = models.CharField(max_length=50)
    minutos_laborados = models.PositiveSmallIntegerField(default=0)
    minutos_aprobados = models.PositiveSmallIntegerField(default=0)
    coordinador_interino = models.BooleanField()
    fecha_fin = models.DateField(blank=True, null=True)
    limitaciones_fisicas = models.TextField(u'Limitaciones físicas',
                                            blank=True, null=True)
    limitaciones_medicas = models.TextField(u'Limitaciones médicas',
                                            blank=True, null=True)
    carrera = models.ForeignKey(u'Carrera')

    def asunto_correo(self):
        mensaje = u'Bienvenido al sistema de Guardabosques USB'

        return mensaje

    def mensaje_correo(self, html=False):
        mensaje = u'Usted se ha registrado exitosamente en el sistema de '\
                  u'Guardabosques USB. El nombre de usuario para acceder '\
                  u'al sistema es %s, y la clave fue la que especificó al '\
                  u'momento del registro.'

        return mensaje % (self.usuario.username if not html else\
                          u'<strong>%s</strong>' % self.usuario.username)

    def __unicode__(self):
        return self.usuario.username

    def save(self, *args, **kwargs):
        if self.minutos_aprobados > self.minutos_laborados:
            raise ValidationError(u'El usuario no puede poseer más tiempo '\
                                  u'aprobado que laborado')

        super(Perfil, self).save(*args, **kwargs)

##
#  Carrera de un estudiante de la USB.
class Carrera(models.Model):
    codigo = models.CharField(max_length=4, unique=True)
    nombre = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.nombre

