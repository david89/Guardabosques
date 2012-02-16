'''
Created on 04/01/2012
Modulo que contiene los formularios del sistema
@author: glpc
'''
from Guardabosques.database.models import Usuario, Actividad, Carrera, Jornada
from django.forms import IntegerField, EmailField, ChoiceField, CharField, PasswordInput, HiddenInput, DateField, DateInput
from django.forms import ModelForm, TextInput, Select, ModelMultipleChoiceField, CheckboxSelectMultiple

class AdminRegistrarUsuarioForm(ModelForm):
    '''
    Formulario del administrador para registrar usuarios
    '''
    correo = EmailField(label=u'Correo Electronico')
    tipo = ChoiceField(label=u'Tipo', choices=[("", "---"), \
                                ("Estudiante", "Estudiante"), \
                                ("Coordinador", "Coordinador"), \
                                ("est_no_act", "Estudiante No Activo")])
    class Meta:
        model = Usuario
        fields = ('cedula', 'correo', 'tipo')
        widgets = {'tipo' : Select(attrs={'class':'selector'})}


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
        model = Usuario
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
