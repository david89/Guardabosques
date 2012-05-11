# -*- coding: utf-8 -*-

"""
Formulario para agregar una jornada
"""

import floppyforms as forms
from django.forms.fields import ChoiceField
from django.forms import RadioSelect
from datetime import date

from Guardabosques.jornada.models import Jornada
from Guardabosques.jornada.models import ESTADO_JORNADA

class SelecFecha(forms.DateInput):
    """ Esta clase es para el widget del calendario """
    template_name = 'floppyforms/SelecFecha.html'

    class Meta:
        js = (
            'js/jquery-ui-1.8.17.custom/js/jquery-ui-1.8.17.custom.min.js',
            'js/jquery-ui-1.8.17.custom/js/jquery-1.7.1.min.js',
        )
        css = {
            'all' : (
                'js/jquery-ui-1.8.17.custom/css/south-street/jquery-ui-1.8.17.custom.css',
            )        
        }

class FormularioEstadoJornada(forms.Form):
    """ Formulario para el estado de las jornadas """
    estado = ChoiceField(widget=RadioSelect, choices=ESTADO_JORNADA)

class FormularioJornada(forms.ModelForm):
    """ Formulario para agregar una jornada """
    fecha = forms.DateField(initial=date.today, widget=SelecFecha)

    def clean(self):
        datos = super(FormularioJornada, self).clean()
        return datos

    class Meta:
        model = Jornada
        exclude = (u'estado', u'perfil', u'actividades')
