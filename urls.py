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


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^time/$', current_date),
    (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
     'django.views.static.serve', {'document_root' : settings.STATIC_ROOT }),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    ## principal
    (r'^principal/$', principal),
    ## Seccion del administrador
    (r'^administrador/$', administrador_base),
    (r'^administrador/registrar_usuario/$', administrador_registrar_usuario),
    (r'^administrador/registrar_usuario_exito/$', administrador_registrar_usuario_exito),
    ## Seccion del estudiante
    (r'^estudiante/$', estudiante_base),
    # Examples:
    # url(r'^$', 'pepe.views.home', name='home'),
    # url(r'^pepe/', include('pepe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
