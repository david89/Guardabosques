from django.conf.urls.defaults import *
from Guardabosques.views import *
from django.conf import settings
# Vistas de login y logout
from django.contrib.auth.views import login, logout
#Admin site
from django.contrib import admin
admin.autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic import list_detail, create_update
from Guardabosques.database.models import Usuario

# Formularios
from formularios.formularios import AdminRegistrarUsuarioForm
usuario_create = {
'form_class' : AdminRegistrarUsuarioForm,
'template_name' : 'administrador/usuarios/registrar_usuario.html',
'post_save_redirect' : 'administrador/usuarios/registrar_usuario_exito.html',
'login_required' : True,
}

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^time/$', current_date),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    ## principal
    (r'^principal/$', principal),
    ## Seccion del administrador

#    (r'^administrador/$', administrador_base),
    
    ## Gestionar Usuario  
#    (r'^administrador/gestionar_usuario/$', administrador_gestionar_usuario),
#    (r'^administrador/consultar_usuario/$', administrador_consultar_usuario),
#    (r'^administrador/registrar_usuario/$', administrador_registrar_usuario),
#    (r'^administrador/registrar_usuario_exito/$', administrador_registrar_usuario_exito),
    
    # Examples:
    # url(r'^$', 'pepe.views.home', name='home'),
    # url(r'^pepe/', include('pepe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

#from Guardabosques.administrador import urls
urlpatterns += patterns('',
    (r'^administrador/', include('Guardabosques.administrador.urls'))
)

#from Guardabosques.estudiante import urls
urlpatterns += patterns('',
    (r'^estudiante/', include('Guardabosques.estudiante.urls'))
)

urlpatterns += patterns('',
(r'^usuarios/create/$', create_update.create_object, usuario_create)
)

