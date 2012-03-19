# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.forms.fields import IntegerField, EmailField, ChoiceField, CharField, PasswordInput, HiddenInput, DateField, DateInput
from django.forms import TextInput, Select, ModelMultipleChoiceField
from django.forms import CheckboxSelectMultiple, RadioSelect
from django.forms import ModelForm, Form

from Guardabosques.jornada.models import Jornada
from Guardabosques.jornada.models import ESTADO_JORNADA


class FormularioEstadoJornada(Form):
    estado = ChoiceField(widget=RadioSelect, choices=ESTADO_JORNADA)

class FormularioJornada(ModelForm):
    estado = ChoiceField(widget=RadioSelect, choices=ESTADO_JORNADA)
    def clean(self):
        datos = super(FormularioJornada, self).clean()
        return datos

    class Meta:
        model = Jornada

