# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$',
        u'Guardabosques.jornada.views.jornadas_pendientes',
        name=u'jornadas_pendientes'),
    url(r'^descripcion/(?P<identificador>\d+)$',
        u'Guardabosques.jornada.views.descripcion_jornada',
        name=u'descripcion_jornada'),
)
