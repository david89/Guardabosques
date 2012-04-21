# -*- coding: utf-8 -*-

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
from usuario.forms import CrearPerfilPendiente, CrearPerfil, EditarPerfil,\
                          EditarPerfilAdministrador

def enviar_correo_usuario_pendiente(perfil, correo):
    mensaje = EmailMultiAlternatives(perfil.asunto_correo(),
                                     perfil.mensaje_correo(),
                                     to=[correo])
    mensaje.attach_alternative(perfil.mensaje_correo(html=True),
                               u'text/html')
    mensaje.send()

def agregar_error_formulario(formulario, error):
    errores = formulario._errors.get('__all__', [])
    errores.append(formulario.error_class([error]))
    formulario._errors['__all__'] = errores

    return formulario

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
                enviar_correo_usuario_pendiente(perfil, perfil.correo)
            except Exception as e:
                perfil.delete()
                error = u'No se pudo agregar el usuario en este momento. Por '\
                        u'favor intente luego nuevamente.'

                formulario = agregar_error_formulario(formulario, error)

                return render_to_response(plantilla,
                                          {u'formulario': formulario},
                                          context_instance=\
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

            # TODO: Cambiar el formulario o el método clean o save del
            # del formulario para que no haya que hacer esto.
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
                enviar_correo_usuario_pendiente(perfil, perfil.usuario.correo)
            except Exception as e:
                perfil.delete()
                usuario.delete()

                error = u'No se pudo agregar el usuario en este momento. Por '\
                        u'favor intente luego nuevamente.'

                formulario = agregar_error_formulario(formulario, error)

                return render_to_response(plantilla,
                                          {u'formulario': formulario},
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

@login_required
def modificar_perfil(request):
    usuario = request.user
    perfil = get_object_or_404(Perfil, usuario=usuario)
    plantilla = u'usuario/modificar_perfil.html'

    if request.method == u'POST':
        formulario = EditarPerfil(request.POST, instance=perfil)
        if formulario.is_valid():
            datos = formulario.cleaned_data

            # TODO: Ver el TODO de regsitrar usuario para disminuir este
            # código.
            usuario.username = datos[u'cedula']
            if (datos[u'clave']):
                usuario.set_password(datos[u'clave'])
            usuario.first_name = datos[u'nombres']
            usuario.last_name = datos[u'apellidos']
            usuario.save()

            perfil.carne = datos[u'carne']
            perfil.telefono_principal = datos[u'telefono_principal']
            perfil.telefono_opcional = datos[u'telefono_opcional']
            perfil.zona = datos[u'zona']
            perfil.limitaciones_fisicas = datos[u'limitaciones_fisicas']
            perfil.limitaciones_medicas = datos[u'limitaciones_medicas']
            perfil.carrera = datos[u'carrera']
            perfil.save()
    else:
        # TODO: Ver el TODO de registrar usuario para disminuir este código.
        datos_usuario = {
            'cedula': usuario.username,
            'nombres': usuario.first_name,
            'apellidos': usuario.last_name
        }
        formulario = EditarPerfil(instance=perfil, initial=datos_usuario)

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
                enviar_correo_usuario_pendiente(perfil, perfil.correo)
            except Exception as e:
                error = u'No se pudo editar el usuario en este momento. Por '\
                        u'favor intente luego nuevamente.'

                formulario = agregar_error_formulario(formulario, error)

                return render_to_response(plantilla,
                                          {u'formulario': formulario},
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

        perfil.usuario.is_active = activo
        perfil.usuario.save()
        perfil.save()

        return render_to_response(exito,
                                  context_instance=RequestContext(request))
    else:
        formulario = EditarPerfilAdministrador()
        formulario.fields.values()[0].initial = perfil.usuario.is_active

    return render_to_response(plantilla,
                              {u'formulario': formulario,
                               u'usuario': perfil},
                               context_instance=RequestContext(request))

@staff_member_required
def eliminar_usuario_pendiente(request, identificador):
    perfil_pendiente = get_object_or_404(PerfilPendiente, pk=identificador)

    perfil_pendiente.delete()

    return HttpResponseRedirect(reverse('listar_usuarios_pendientes'))
