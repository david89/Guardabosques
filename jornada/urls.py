# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic import DetailView

from Guardabosques.jornada.models import Jornada
from Guardabosques.jornada.views import DetallesJornada

urlpatterns = patterns('',
    url(r'^$',
        u'Guardabosques.jornada.views.moderar_jornadas',
        name=u'moderar_jornadas'),
    url(r'^(?P<tipo_jornada>\w+)/$',
        u'Guardabosques.jornada.views.administrar_jornadas',
        name=u'administrar_jornadas'),
    url(r'^agregar$',
        u'Guardabosques.jornada.views.agregar_jornada',
        name=u'agregar_jornada'),
    url(r'^editar/(?P<jornada_pk>\d+)$',
        u'Guardabosques.jornada.views.agregar_jornada',
        name=u'editar_jornada'),
    url(r'^eliminar/(?P<jornada_pk>\d+)$',
        u'Guardabosques.jornada.views.eliminar_jornada',
        name=u'eliminar_jornada'),
    url(r'^detalles/(?P<pk>\d+)$',
        DetallesJornada.as_view(template_name='jornada/descripcion_jornada.html'),
        name=u'detalles_jornada'),
)
