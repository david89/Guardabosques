from django.conf.urls.defaults import *
from django.conf import settings

# Vista de la seccion de Administrador
from Guardabosques.estudiante.views import *

urlpatterns = patterns('',
    (r'^$', estudiante_base),
)

#from Guardabosques.administrador.usuarios import urls
# Gestionar Usuario
urlpatterns += patterns('',
    (r'^usuarios/', include('Guardabosques.estudiante.usuarios.urls')),                  
)

# Gestionar Jornadas
urlpatterns += patterns('',
    (r'^jornada/', include('Guardabosques.estudiante.jornada.urls')),                  
)