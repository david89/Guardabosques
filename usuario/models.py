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

# NOTA: cedula, nombres, apellidos, clave y email en user.
##
#  Perfil que es creado por un coordinador.
class PerfilPendiente(models.Model):
    cedula = models.CharField(u'Cédula de identidad', max_length=8,
                              unique=True)
    correo = models.EmailField(u'Correo electrónico', unique=True)
    tipo = models.CharField(choices=USUARIO_TIPOS, max_length=1)
    estado = models.CharField(choices=USUARIO_ESTADOS, max_length=1)
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
                  u'de guardabosques de la USB. Si su cédula de identidad '\
                  u'es %s por favor ingrese al siguiente enlace: %s. De lo '\
                  u'contrario notifique al administrador del sistema acerca '\
                  u'del error.'

        enlace = "http://%s%s" % (settings.SITE_URL,
                                  reverse(u'registrar_usuario',
                                          args=[self.verificador]))

        return mensaje % (self.cedula if not html else
                            u'<strong>%s</strong>' % (self.cedula),
                          enlace if not html else
                            u'<a href=%s>%s</a>' % (enlace, enlace))

    ##
    #  Operación guardar de la clase. El verificador se compone de la cédula
    #  de identidad del perfil pendiente junto con la fecha de creación del
    #  perfil pendiente.
    def save(self, *args, **kwargs):
        self.verificador = sha256(u'%s$%s' %
                            (self.cedula, datetime.now())).hexdigest()

        super(PerfilPendiente, self).save(*args, **kwargs)

