'''
Created on 04/01/2012
Modulo que contiene los formularios del sistema
@author: glpc
'''
from django import forms
from django.forms import ModelForm

class AdminRegistrarUsuarioForm(forms.Form):
    '''
    Formulario del administrador para registrar usuarios
    '''
    cedula = forms.IntegerField(label=u'Cedula')
    correo = forms.EmailField(label=u'Correo Electronico', max_length=50)
    tipo = forms.ChoiceField(choices=[("est_act","Estudiante"),\
                                      ("est_no_act","Estudiante No Activo"),\
                                      ("coord","Coordinador")], \
                                      widget=forms.Select(attrs={'class':'selector'}),\
                                      label='Tipo')
