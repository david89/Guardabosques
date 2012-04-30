# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$',
        u'Guardabosques.jornada.views.administrar_jornadas',
        name=u'administrar_jornadas'),
)
