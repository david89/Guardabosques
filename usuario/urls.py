from django.conf.urls.defaults import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list

from models import Perfil, PerfilPendiente

urlpatterns = patterns(u'',
    url(r'^$',
        staff_member_required(direct_to_template),
        {u'template': u'usuario/gestionar.html'},
        name=u'gestionar_usuarios'),
    url(r'^agregar/$',
        u'Guardabosques.usuario.views.agregar_usuario',
        name=u'agregar_usuario'),
    url(r'^registrar_usuario/(?P<verificador>\w+)/$',
        u'Guardabosques.usuario.views.registrar_usuario',
        name=u'registrar_usuario'),
    url(r'^listar_usuarios$',
        staff_member_required(object_list),
        {u'queryset': Perfil.objects.all().order_by('pk'),
         u'template_name': u'usuario/listar_usuarios.html',
         u'template_object_name': u'perfiles',},
        name=u'listar_usuarios'),
    url(r'^listar_usuarios_pendientes$',
        staff_member_required(object_list),
        {u'queryset': PerfilPendiente.objects.all(),
         u'template_name': u'usuario/listar_usuarios_pendientes.html',
         u'template_object_name': u'perfiles_pendientes',},
        name=u'listar_usuarios_pendientes'),
    url(r'^editar_usuario_pendiente/(?P<identificador>\d+)/$',
        u'Guardabosques.usuario.views.editar_usuario_pendiente',
        name=u'editar_usuario_pendiente'),
    url('^editar_usuario_administrador/(?P<identificador>\d+)/$',
        u'Guardabosques.usuario.views.editar_usuario_administrador',
        name=u'editar_usuario_administrador'),
    url('^modificar_perfil/$',
        u'Guardabosques.usuario.views.modificar_perfil',
        name=u'modificar_perfil'),
    url(r'^eliminar_usuario_pendiente/(?P<identificador>\d+)/$',
        u'Guardabosques.usuario.views.eliminar_usuario_pendiente',
        name=u'eliminar_usuario_pendiente'),
    url(r'^iniciar_sesion/',
        u'django.contrib.auth.views.login',
        {u'template_name': u'usuario/iniciar_sesion.html'},
        name=u'iniciar_sesion'),
    url(r'^finalizar_sesion/',
        u'django.contrib.auth.views.logout',
        {u'next_page': u'/'},
        name=u'finalizar_sesion'),
    url(r'^jornadas_de_trabajo/(?P<tipo>\w+)$',
        u'Guardabosques.usuario.views.jornadas_de_trabajo',
        name=u'jornadas_de_trabajo'),
    url(r'^jornadas_de_trabajo$',
        u'Guardabosques.usuario.views.jornadas_de_trabajo',
        name=u'jornadas_de_trabajo'),
)

