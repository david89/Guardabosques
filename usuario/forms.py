# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.forms import IntegerField, EmailField, ChoiceField, CharField, PasswordInput, HiddenInput, DateField, DateInput
from django.forms import TextInput, Select, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.forms import ModelForm

from Guardabosques.usuario.models import PerfilPendiente

##
#  Formulario del administrador para registrar usuarios
class CrearPerfilPendiente(ModelForm):
    def clean(self):
        datos = super(CrearPerfilPendiente, self).clean()

        # Todo estudiante debe poseer un estado.
        if datos[u'tipo'] == u'E' and (datos[u'estado'] == u''
           or datos[u'estado'] is None):
            raise ValidationError(u'El estado debe ser indicado para todo '
                                  u'estudiante.')

        return datos

    class Meta:
        model = PerfilPendiente
        exclude = (u'verificador', u'fecha_creacion')

