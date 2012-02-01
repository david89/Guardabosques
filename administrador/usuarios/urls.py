from django.conf.urls.defaults import *
from django.conf import settings

# Vista de la seccion de Administrador
from Guardabosques.administrador.usuarios.views import *


# Gestionar Usuario
urlpatterns = patterns('',
    (r'^$', gestionar_usuario),
    (r'^consultar_usuario/$', consultar_usuario),
    (r'^registrar_usuario/$', registrar_usuario),
    (r'^registrar_usuario_exito/$', registrar_usuario_exito),
    (r'^eliminar_usuario/(?P<cedula>\d+)/$', eliminar_usuario),
    (r'^modificar_usuario/(?P<cedula>\d+)/$', modificar_usuario),
    (r'^modificar_usuario/$', modificar_usuario,{'cedula': ''}),
    (r'^modificar_usuario_exito/$', modificar_usuario_exito),              
)   