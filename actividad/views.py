from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from actividad.models import Actividad
from actividad.forms import FormularioActividad

def listar_actividades(request):
    plantilla = u'actividad/listar_actividades.html'
    actividades = Actividad.objects.all()
    return render_to_response(plantilla, {u'actividades' : actividades},
                              context_instance=RequestContext(request))


def eliminar_actividad(request, identificador):
    actividad = Actividad.objects.get(id=identificador)
    actividad.delete()
    return listar_actividades(request)

def agregar_actividad(request):
    plantilla = u'actividad/agregar_actividad.html'
    if request.method == 'POST':
        formulario = FormularioActividad(request.POST)
        if formulario.is_valid():
            formulario.save()
            return listar_actividades(request)
    else:
        formulario = FormularioActividad()

    return render_to_response(plantilla,
                              {'formulario': formulario},
                              context_instance=RequestContext(request))

def editar_actividad(request, identificador):
    plantilla = u'actividad/editar_actividad.html'
    actividad = Actividad.objects.get(id=identificador)
    if request.method == 'POST':
        formulario = FormularioActividad(request.POST, instance=actividad)
        if formulario.is_valid():
            formulario.save()
            return listar_actividades(request)
    else:
        formulario = FormularioActividad(instance=actividad)
    return render_to_response(plantilla,
                              {'formulario': formulario},
                              context_instance=RequestContext(request))
