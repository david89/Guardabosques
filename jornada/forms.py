# -*- coding: utf-8 -*-

"""
Formulario para agregar una jornada
"""
import datetime
import floppyforms as forms
from django.forms.fields import ChoiceField
from django.forms import RadioSelect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, ButtonHolder

from Guardabosques.jornada.models import Jornada, ConstituidaPor
from Guardabosques.jornada.models import ESTADO_JORNADA
from Guardabosques.jornada.widgets import SplitTimeField, SplitTimeWidget

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
                'js/jquery-ui-1.8.17.custom/css/south-street/'
                'jquery-ui-1.8.17.custom.css',
            )
        }

class FormularioActividad(forms.ModelForm):
    """ Formulario para agregar una actividad """
    class Meta:
        model = ConstituidaPor
        exclude = (u'jornada')


class FormularioEstadoJornada(forms.Form):
    """ Formulario para el estado de las jornadas """
    estado = ChoiceField(widget=RadioSelect, choices=ESTADO_JORNADA)

class FormularioJornada(forms.ModelForm):
    """ Formulario para agregar una jornada """
    fecha = forms.DateField(widget=SelecFecha(), input_formats=['%d-%m-%Y'])
    hora_inicio = SplitTimeField(widget=SplitTimeWidget)
    hora_fin = SplitTimeField(widget=SplitTimeWidget)

    def clean(self):
        super(FormularioJornada, self).clean()
        print self.cleaned_data
        return self.cleaned_data

    @property
    def helper(self):
        """ This method is used by crispy tag """
        helper = FormHelper()
        helper.form_method = 'post'
        helper.layout = Layout(
                Div(
                    'fecha',
                    'hora_inicio',
                    'hora_fin'
                ),
            )
        return helper

    class Meta:
        model = Jornada
        exclude = (u'estado', u'perfil', u'actividades')
