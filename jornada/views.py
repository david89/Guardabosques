from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from jornada.models import Jornada, ConstituidaPor
from usuario.models import Perfil
from jornada.forms import FormularioJornada

@staff_member_required
def jornadas_pendientes(request):
    """
    Lista las jornadas pertenecientes de los usuarios.
    """
    plantilla = u'jornada/jornadas_pendientes.html'
    jornadas = Jornada.objects.filter(estado=u'P')
    if request.method == 'POST':
        for jornada in jornadas:
            jornada.estado =  request.POST.get('%s' % jornada.pk)
            jornada.save()
    return render_to_response(plantilla, {u'jornadas' : jornadas},
                              context_instance=RequestContext(request))

def descripcion_jornada(request, identificador):
    plantilla = u'jornada/descripcion_jornada.html'
    j = Jornada.objects.get(id=identificador)
    detalles = ConstituidaPor.objects.filter(jornada=j)
    return render_to_response(plantilla, {u'detalles' : detalles},
                              context_instance=RequestContext(request))

@login_required
def administrar_jornadas(request):
    """
    Lista las jornadas que posee el usuario.
    """
    plantilla = u'jornada/jornadas_de_trabajo.html'
    perfil_usuario = Perfil.objects.get(usuario__id=request.user.pk)
    jornadas = Jornada.objects.filter(perfil__id=perfil_usuario.pk)
    return render_to_response(plantilla, {u'jornadas' : jornadas, 
                                          u'tipo' : "pendiente"},
                              context_instance=RequestContext(request))

@login_required
def agregar_jornada(request):
    """ Agregar una nueva jornada """
    plantilla = u'jornada/agregar_jornada.html'
    formulario = FormularioJornada()
    return render_to_response(plantilla, 
                              {u'formulario' : formulario},
                              context_instance=RequestContext(request))
