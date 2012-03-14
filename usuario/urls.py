from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.list_detail import object_list

# Vista de la seccion de Administrador
from Guardabosques.administrador.usuarios.views import *

# Gestionar Usuario
urlpatterns = patterns('',
    url(r'^$', gestionar_usuario),
    url(r'^crear_usuario/$',
        crear_usuario,
        name=u'crear_usuario'),
    url(r'^consultar_pendientes/$',
        consultar_pendientes,
        name=u'consultar_pendientes'),
    url(r'^registro/(?P<verificador>\w+)/$',
        registrar_usuario,
        name=u'registro'),
#    (r'^eliminar_usuario/(?P<cedula>\d+)/$', eliminar_usuario),
#    (r'^modificar_usuario/(?P<cedula>\d+)/$', modificar_usuario),
#    (r'^modificar_usuario/$', modificar_usuario,{'cedula': ''}),
#    (r'^modificar_usuario_exito/$', modificar_usuario_exito),              
)   
