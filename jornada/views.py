from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from jornada.models import Jornada, ConstituidaPor

def jornadas_pendientes(request):
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
