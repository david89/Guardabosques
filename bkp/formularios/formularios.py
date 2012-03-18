# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.forms import IntegerField, EmailField, ChoiceField, CharField, PasswordInput, HiddenInput, DateField, DateInput
from django.forms import ModelForm, TextInput, Select, ModelMultipleChoiceField, CheckboxSelectMultiple

from Guardabosques.usuario.models import PerfilPendiente
from Guardabosques.database.models import Perfil, Actividad, Carrera, Jornada

###
##  Formulario del administrador para registrar usuarios
#class FormularioCrearPerfilPendiente(ModelForm):
#    class Meta:
#        model = PerfilPendiente
#        exclude = (u'verificador', u'fecha_creacion')

class AdminRegistrarActividadForm(ModelForm):
    '''
    Formulario del administrador para registrar actividades
    '''
    class Meta:
        model = Actividad

class EstModificarUsuarioForm(ModelForm):
    '''
    Formulario del usuario para modifical sus datos
    '''
    class Meta:
        #model = Usuario
        exclude = ('clave', 'estado', 'tipo', 'horas_laboradas', 'horas_aprobadas', 'fecha_fin', 'fecha_inicio')
        
class EstRegistrarJornadaForm(ModelForm):
    '''
    Formulario para registrar las jornadas
    '''
    actividad = ModelMultipleChoiceField(label=u'Actividad', queryset=Actividad.objects.all(), widget=CheckboxSelectMultiple)
    cedula_usuario = IntegerField(widget=HiddenInput,required=False)
    class Meta:
        model = Jornada
        fields = ('fecha', 'minutos')
        #widgets = {'identificador' : HiddenInput()}
