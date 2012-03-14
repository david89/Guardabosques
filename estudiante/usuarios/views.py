from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# Decoradores
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Modelos
#from database.models import Usuario

# Formularios
from formularios.formularios import EstModificarUsuarioForm

# Usuarios
from django.contrib.auth.models import User

@csrf_exempt
@login_required
def modificar_usuario(request):
    if request.method == 'POST':
        try:
            print "1"
            cedula = request.user.username
            usuario = Usuario.objects.get(cedula=cedula)
            django_user = User.objects.get(username=cedula)
        except Usuario.DoesNotExist:
            print "error usuario no eixsteD"
            return render_to_response("estudiante/usuarios/modificar_usuario.html",\
                                      {'error':cedula, 'tipo' : 'Usuario'})
        except User.DoesNotExist:
            print "error django usuario no eixsteD"
            return render_to_response("estudiante/usuarios/modificar_usuario.html",\
                                          {'error':cedula, 'tipo' : 'DJango USer'})
        else:
            formulario = EstModificarUsuarioForm(request.POST,instance= usuario)
            if formulario.is_valid():
                form_usuario = formulario.cleaned_data
                if django_user.email != form_usuario['correo']:
                    django_user.email = form_usuario['correo']
                django_user.save()
                formulario.save()
                return HttpResponseRedirect("/estudiante/usuarios/modificar_usuario_exito/")
            else:
                return render_to_response("estudiante/usuarios/modificar_usuario_exito.html",\
                                              {'error':cedula, 'tipo' : 'DJango USer'})
    else:
        try:
            print request.user.username
            usuario = Usuario.objects.get(cedula=request.user.username)
        except Usuario.DoesNotExist:
            return render_to_response("estudiante/usuarios/modificar_usuario.html",\
                                      {'error':request.user.username, 'tipo' : 'Usuario'})
        else:
            formulario = EstModificarUsuarioForm(instance = usuario)
            return render_to_response("estudiante/usuarios/modificar_usuario.html", \
                              {'form': formulario}) 

@login_required
def modificar_usuario_exito(request):
    return render_to_response("estudiante/usuarios/modificar_usuario_exito.html")
