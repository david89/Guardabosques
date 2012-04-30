# -*- coding: utf-8 -*-

"""
Formulario para agregar una jornada
"""

from django.forms.fields import ChoiceField
from django.forms import RadioSelect
from django.forms import ModelForm, Form

from Guardabosques.jornada.models import Jornada
from Guardabosques.jornada.models import ESTADO_JORNADA


class FormularioEstadoJornada(Form):
    """ Formulario para el estado de las jornadas """
    estado = ChoiceField(widget=RadioSelect, choices=ESTADO_JORNADA)

class FormularioJornada(ModelForm):
    """ Formulario para agregar una jornada """
    def clean(self):
        datos = super(FormularioJornada, self).clean()
        return datos

    class Meta:
        model = Jornada
        exclude = (u'estado', u'perfil')

