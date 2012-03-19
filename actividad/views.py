from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from actividad.models import Actividad

def listar_actividades(request):
    plantilla = u'actividad/listar_actividades.html'
    actividades = Actividad.objects.all()
    return render_to_response(plantilla, {u'actividades' : actividades},
                              context_instance=RequestContext(request))


def eliminar_actividad(request, identificador):
    actividad = Actividad.objects.filter(id=identificador)[0]
    actividad.delete()
    return listar_actividades(request)
