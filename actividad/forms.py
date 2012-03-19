# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.forms import IntegerField, EmailField, ChoiceField, CharField, PasswordInput, HiddenInput, DateField, DateInput
from django.forms import TextInput, Select, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.forms import ModelForm

from Guardabosques.actividad.models import Actividad

##
#  Formulario del administrador para registrar usuarios
class FormularioActividad(ModelForm):
    def clean(self):
        datos = super(FormularioActividad, self).clean()
        return datos

    class Meta:
        model = Actividad

