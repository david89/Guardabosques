# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$',
        u'Guardabosques.actividad.views.listar_actividades',
        name=u'listar_actividades'),
    url(r'^eliminar/(?P<identificador>\d+)$', 
        u'Guardabosques.actividad.views.eliminar_actividad',
        name=u'eliminar_actividad'),
)
