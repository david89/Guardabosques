from django.conf.urls.defaults import *
from django.conf import settings

# Vista de la seccion de Administrador
from Guardabosques.administrador.views import *

urlpatterns = patterns('',
    (r'^$', administrador_base),
)

#from Guardabosques.administrador.usuarios import urls
# Gestionar Usuario
urlpatterns += patterns('',
    (r'^usuarios/', include('Guardabosques.administrador.usuarios.urls')),                  
)

# Gestionar Actividades
urlpatterns += patterns('',
    (r'^actividad/', include('Guardabosques.administrador.actividad.urls')),                  
)  