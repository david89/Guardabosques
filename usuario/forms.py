# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput

from Guardabosques.usuario.models import PerfilPendiente, Perfil

##
#  Formulario del administrador para registrar usuarios.
class CrearPerfilPendiente(ModelForm):
    def clean(self):
        datos = super(CrearPerfilPendiente, self).clean()

        if Perfil.objects.filter(usuario__email=datos[u'correo']).exists():
            raise ValidationError(u'Ya existe un usuario registrado en el '
                                  u'sistema con ese correo electrónico')

        return datos

    class Meta:
        model = PerfilPendiente
        exclude = (u'verificador', u'fecha_creacion')

##
#  Formulario de los perfiles de estudiantes o coordinadores interinos.
class CrearPerfil(ModelForm):
    cedula = CharField(label=u'Cédula', max_length=8)
    nombres = CharField(max_length=30)
    apellidos = CharField(max_length=30)
    clave = CharField(widget=PasswordInput)
    confirmar_clave = CharField(widget=PasswordInput)

    def clean(self):
        datos = super(CrearPerfil, self).clean()

        if Perfil.objects.filter(usuario__username=datos[u'cedula']).exists():
            raise ValidationError(u'Ya existe un usuario registrado con esa '
                                  u'cédula de identidad')

        return datos

    class Meta:
        model = Perfil
        fields = (u'cedula', u'nombres', u'apellidos', u'clave',
                  u'confirmar_clave', u'carne', u'carrera',
                  u'telefono_principal', u'telefono_opcional', u'zona',
                  u'limitaciones_fisicas', u'limitaciones_medicas')

