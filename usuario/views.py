from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from usuario.models import PerfilPendiente
from usuario.forms import CrearPerfilPendiente

@login_required
def agregar_usuario(request):
    plantilla = u'usuario/agregar_usuario.html'
    exito = u'usuario/agregar_usuario_exito.html'

    if request.method == 'POST':
        formulario = CrearPerfilPendiente(request.POST)
        if formulario.is_valid():
            formulario.save()
            perfil = formulario.instance

            # Se intenta enviar un correo a la persona.
            try:
                mensaje = EmailMultiAlternatives(perfil.asunto_correo(),
                                                 perfil.mensaje_correo(),
                                                 to=[perfil.correo])
                mensaje.attach_alternative(perfil.mensaje_correo(html=True),
                                           u'text/html')
                mensaje.send()
            except Exception as e:
                perfil.delete()
                return render_to_response(plantilla,
                                          {u'formulario': formulario,
                                           u'error': u'No se pudo agregar el '
                                                     u'usuario en este '
                                                     u'momento. Por favor '
                                                     u'intente luego '
                                                     u'nuevamente.'},
                                          context_instance=
                                            RequestContext(request))

            return render_to_response(exito,
                                      context_instance=RequestContext(request))
    else:
        formulario = CrearPerfilPendiente()

    return render_to_response(plantilla,
                              {'formulario': formulario},
                              context_instance=RequestContext(request))

@csrf_exempt
def registrar_usuario(request):
    pass

