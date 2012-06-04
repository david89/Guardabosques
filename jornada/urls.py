# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$',
        u'Guardabosques.jornada.views.administrar_jornadas',
        name=u'administrar_jornadas'),
    url(r'^agregar$',
        u'Guardabosques.jornada.views.agregar_jornada',
        name=u'agregar_jornada'),
    url(r'^eliminar/(?P<jornada_pk>\d+)$',
        u'Guardabosques.jornada.views.eliminar_jornada',
        name=u'eliminar_jornada'),
)
