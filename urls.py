 # -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
#from django.views.generic.simple import direct_to_template

urlpatterns = patterns(u'',
    url(r'^$',
        u'Guardabosques.views.inicio',
        name=u'inicio'),
    url(r'^usuario/', include(u'Guardabosques.usuario.urls')),
    url(r'^actividad/', include(u'Guardabosques.actividad.urls')),
)

#urlpatterns += patterns('',
#    (r'^administrador/', include('Guardabosques.administrador.urls'))
#)

#from django.conf.urls.defaults import *
#from Guardabosques.views import *
#from django.conf import settings
## Vistas de login y logout
#from django.contrib.auth.views import login, logout
##Admin site
#from django.contrib import admin
#admin.autodiscover()
#
#
## Uncomment the next two lines to enable the admin:
## from django.contrib import admin
## admin.autodiscover()
#from django.views.generic import list_detail, create_update
#from Guardabosques.usuario.models import PerfilPendiente
#
## Formularios
#from Guardabosques.usuario.forms import CrearPerfilPendiente
#usuario_create = {
#    'form_class': CrearPerfilPendiente,
#    'template_name': 'administrador/usuarios/registrar_usuario.html',
#    'post_save_redirect': 'administrador/usuarios/registrar_usuario_exito.html',
#    'login_required': True,
#}
#
#urlpatterns = patterns('',
#    (r'^admin/', include(admin.site.urls)),
#    (r'^accounts/login/$', login),
#    (r'^accounts/logout/$', logout),
#    (r'^$', principal),
#    (r'^usuario/$', include(u'Guardabosques.usuario.urls')),
#)
#
##from Guardabosques.administrador import urls
#urlpatterns += patterns('',
#    (r'^administrador/', include('Guardabosques.administrador.urls'))
#)
#
##from Guardabosques.estudiante import urls
#urlpatterns += patterns('',
#    (r'^estudiante/', include('Guardabosques.estudiante.urls'))
#)
#
#urlpatterns += patterns('',
#(r'^usuarios/create/$', create_update.create_object, usuario_create)
#)
#
