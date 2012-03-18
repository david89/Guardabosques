from django.conf.urls.defaults import *
from django.conf import settings

# Vista de la seccion del Estudiante
from Guardabosques.estudiante.usuarios.views import *


# Gestionar Usuario
urlpatterns = patterns('',
    (r'^modificar_usuario/$', modificar_usuario),
    (r'^modificar_usuario_exito/$', modificar_usuario_exito),              
)   