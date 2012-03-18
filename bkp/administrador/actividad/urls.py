from django.conf.urls.defaults import *
from django.conf import settings

# Vista de la seccion de estudiante
from Guardabosques.administrador.actividad.views import *


# Gestionar Actividades
urlpatterns = patterns('',
    (r'^$', gestionar_actividad),
    (r'^consultar_actividad/$', consultar_actividad),
    (r'^registrar_actividad/$', registrar_actividad),
    (r'^registrar_actividad_exito/$', registrar_actividad_exito),
    (r'^eliminar_actividad/(?P<nombre>[\s\w]+)/$', eliminar_actividad),
    (r'^modificar_actividad/(?P<nombre>[\s\w]+)/$', modificar_actividad),
    (r'^modificar_actividad/$', modificar_actividad,{'nombre': ''}),
    (r'^modificar_actividad_exito/$', modificar_actividad_exito),            
)
