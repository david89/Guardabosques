from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from usuario.models import PerfilPendiente
from usuario.forms import CrearPerfilPendiente

@login_required
def crear_usuario(request):
    plantilla = u'administrador/usuarios/crear_usuario.html'
    exito = u'administrador/usuarios/crear_usuario_exito.html'

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
            except:
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

@login_required
def consultar_usuario(request):
    usuarios = PerfilPendiente.objects.all()

    return render_to_response("administrador/usuarios/consultar_usuario.html",\
                              {'usuarios': usuarios},
                              context_instance=RequestContext(request))

@login_required
def gestionar_usuario(request):
    return render_to_response("administrador/usuarios/gestionar_usuario.html")



def registrar_usuario(request, verificador):
    pass

@login_required
def eliminar_usuario(request, cedula):
    try:
        cedula = int(cedula)
    except ValueError:
        return render_to_response("administrador/usuarios/eliminar_usuario.html",\
                                  {'error': cedula, 'tipo' : 'No entero'})
    try:
        str_cedula = str(cedula)
        usuario = Usuario.objects.get(cedula=str_cedula)
        django_user = User.objects.get(username=str_cedula)
    except Usuario.DoesNotExist:
        print "error usuario no eixste User"
        return render_to_response("administrador/usuarios/eliminar_usuario.html",\
                                  {'error':cedula, 'tipo' : 'Usuario'})
    except User.DoesNotExist:
        print "error usuario no eixste Django"
        return render_to_response("administrador/usuarios/eliminar_usuario.html",\
                                  {'error':cedula, 'tipo' : 'DJango USer'})
    else:
        usuario.delete()
        django_user.delete()
        return render_to_response("administrador/usuarios/eliminar_usuario.html")

@csrf_exempt
@login_required
def modificar_usuario(request,cedula):
    if request.method == 'POST':
        print request.POST
        if 'cedula' in request.POST:
            cedula = request.POST['cedula']

        else:
            print "ceulda no entero"
            return render_to_response("administrador/usuarios/modificar_usuario_exito.html",\
                                      {'error':cedula, 'tipo' : 'Usuario'})
        try:
            usuario = Usuario.objects.get(cedula=cedula)
            django_user = User.objects.get(username=cedula)
        except Usuario.DoesNotExist:
            print "error usuario no eixsteD"
            return render_to_response("administrador/usuarios/modificar_usuario_exito.html",\
                                      {'error':cedula, 'tipo' : 'Usuario'})
        except User.DoesNotExist:
            print "error django usuario no eixsteD"
            return render_to_response("administrador/usuarios/modificar_usuario_exito",\
                                          {'error':cedula, 'tipo' : 'DJango USer'})
        else:
            formulario = AdminRegistrarUsuarioForm(request.POST,instance= usuario)
            print formulario.is_valid()
            if formulario.is_valid():
                form_usuario = formulario.cleaned_data
                if django_user.email != form_usuario['correo']:
                    usuario.correo = form_usuario['correo']
                    django_user.email = form_usuario['correo']
                tipo_usuario = form_usuario['tipo']
                if  tipo_usuario == 'Coordinador': # Si el usuario es un coordinador
                    usuario.tipo = u'Coordinador'
                    usuario.estado = u'Activo'
                else:
                    usuario.tipo = u'Estudiante'
                    if tipo_usuario == 'Estudiante':
                        usuario.estado = u'Activo'
                    else:
                        usuario.estado = u'Inactivo'
                usuario.save()
                django_user.save()
                return HttpResponseRedirect("/administrador/usuarios/modificar_usuario_exito/")
            else:
                return render_to_response("administrador/usuarios/modificar_usuario_exito.html",\
                                              {'error':cedula, 'tipo' : 'DJango USer'})
    else:
        try:
            cedula = int(cedula)
        except ValueError:
            return render_to_response("administrador/usuarios/modificar_usuario.html",\
                                      {'error': cedula, 'tipo' : 'No entero'})
        try:
            str_cedula = str(cedula)
            usuario = Usuario.objects.get(cedula=str_cedula)
        except Usuario.DoesNotExist:
            return render_to_response("administrador/usuarios/modificar_usuario.html",\
                                      {'error':cedula, 'tipo' : 'Usuario'})
        else:
            formulario = AdminRegistrarUsuarioForm(instance = usuario)
            return render_to_response("administrador/usuarios/modificar_usuario.html", \
                              {'form': formulario})

@login_required
def modificar_usuario_exito(request):
    return render_to_response("administrador/usuarios/modificar_usuario_exito.html")
