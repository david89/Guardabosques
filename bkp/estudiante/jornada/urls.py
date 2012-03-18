from django.conf.urls.defaults import *
from django.conf import settings

# Vista de la seccion de Administrador
from Guardabosques.estudiante.jornada.views import *


# Gestionar jornadaes
urlpatterns = patterns('',
    (r'^$', gestionar_jornada),
    (r'^consultar_jornada/$', consultar_jornada),
    (r'^registrar_jornada/$', registrar_jornada),
    (r'^registrar_jornada_exito/$', registrar_jornada_exito),
#    (r'^eliminar_jornada/(?P<nombre>[\s\w]+)/$', eliminar_jornada),
#    (r'^modificar_jornada/(?P<nombre>[\s\w]+)/$', modificar_jornada),
#    (r'^modificar_jornada/$', modificar_jornada,{'nombre': ''}),
#    (r'^modificar_jornada_exito/$', modificar_jornada_exito),            
)   