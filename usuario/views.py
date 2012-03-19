from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from usuario.models import PerfilPendiente, Perfil
from usuario.forms import CrearPerfilPendiente, CrearPerfil, \
                          EditarPerfilAdministrador

@staff_member_required
def agregar_usuario(request):
    plantilla = u'usuario/agregar_usuario.html'
    exito = u'usuario/agregar_usuario_exito.html'

    if request.method == u'POST':
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
def registrar_usuario(request, verificador):
    perfil_pendiente =\
        get_object_or_404(PerfilPendiente, verificador=verificador)
    
    plantilla = u'usuario/registrar_usuario.html'
    exito = u'usuario/registrar_usuario_exito.html'

    if request.method == u'POST':
        formulario = CrearPerfil(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data

            usuario = User.objects.create_user(datos[u'cedula'],
                                               perfil_pendiente.correo,
                                               datos[u'clave'])
            usuario.first_name = datos[u'nombres']
            usuario.last_name = datos[u'apellidos']
            usuario.is_active = perfil_pendiente.activo
            usuario.save()

            perfil = Perfil(usuario=usuario,
                            carne=datos[u'carne'],
                            telefono_principal=\
                                datos[u'telefono_principal'],
                            telefono_opcional=\
                                datos[u'telefono_opcional'],
                            zona=datos[u'zona'],
                            coordinador_interino=\
                                perfil_pendiente.coordinador,
                            limitaciones_fisicas=\
                                datos[u'limitaciones_fisicas'],
                            limitaciones_medicas=\
                                datos[u'limitaciones_medicas'],
                            carrera=datos[u'carrera'])
            perfil.save()

            # Se intenta enviar un correo a la persona.
            try:
                mensaje = EmailMultiAlternatives(perfil.asunto_correo(),
                                                 perfil.mensaje_correo(),
                                                 to=[perfil.usuario.email])
                mensaje.attach_alternative(perfil.mensaje_correo(html=True),
                                           u'text/html')
                mensaje.send()
            except Exception as e:
                perfil.delete()
                usuario.delete()
                return render_to_response(plantilla,
                                          {u'formulario': formulario,
                                           u'error': u'No se pudo agregar el '
                                                     u'usuario en este '
                                                     u'momento. Por favor '
                                                     u'intente luego '
                                                     u'nuevamente.'},
                                          context_instance=
                                            RequestContext(request))

            perfil_pendiente.delete()
            usuario = authenticate(username=datos[u'cedula'],
                                   password=datos[u'clave'])
            login(request, usuario)

            return HttpResponseRedirect(reverse(u'inicio'))
    else:
        formulario = CrearPerfil()

    return render_to_response(plantilla,
                              {u'formulario': formulario},
                              context_instance=RequestContext(request))

@staff_member_required
def editar_usuario_pendiente(request, identificador):
    perfil_pendiente = get_object_or_404(PerfilPendiente, pk=identificador)
    plantilla = u'usuario/editar_usuario.html'
    exito = u'usuario/editar_usuario_exito.html'

    if request.method == u'POST':
        formulario = CrearPerfilPendiente(request.POST, instance=perfil_pendiente)
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
                                           u'error': u'No se pudo editar el '
                                                     u'usuario en este '
                                                     u'momento. Por favor '
                                                     u'intente luego '
                                                     u'nuevamente.'},
                                          context_instance=
                                            RequestContext(request))

            return render_to_response(exito,
                                      context_instance=RequestContext(request))
    else:
        formulario = CrearPerfilPendiente(instance=perfil_pendiente)

    return render_to_response(plantilla,
                              {'formulario': formulario},
                              context_instance=RequestContext(request))

@staff_member_required
def editar_usuario_administrador(request, identificador):
    perfil = get_object_or_404(Perfil, pk=identificador)
    plantilla = u'usuario/editar_usuario_administrador.html'
    exito = u'usuario/editar_usuario_administrador_exito.html'

    if request.method == u'POST':
        formulario = EditarPerfilAdministrador(request.POST)
        activo = bool(request.POST.get('activo', False))
        coordinador = bool(request.POST.get('coordinador', False))

        perfil.usuario.is_active = activo
        perfil.usuario.save()
        perfil.coordinador_interino = coordinador
        perfil.save()

        return render_to_response(exito,
                                  context_instance=RequestContext(request))
    else:
        formulario = EditarPerfilAdministrador()
        formulario.fields.values()[0].initial = perfil.usuario.is_active
        formulario.fields.values()[1].initial = perfil.coordinador_interino

    return render_to_response(plantilla,
                              {u'formulario': formulario,
                               u'usuario': perfil},
                               context_instance=RequestContext(request))

@staff_member_required
def eliminar_usuario_pendiente(request, identificador):
    perfil_pendiente = get_object_or_404(PerfilPendiente, pk=identificador)

    perfil_pendiente.delete()

    return HttpResponseRedirect(reverse('listar_usuarios_pendientes'))

