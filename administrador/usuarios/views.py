from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# Decoradores
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

#Email
from django.core.mail import EmailMessage

# Modelos
from database.models import Usuario

# Formularios
from formularios.formularios import AdminRegistrarUsuarioForm

# Usuarios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


@login_required
def gestionar_usuario(request):
    return render_to_response("administrador/usuarios/gestionar_usuario.html")

@csrf_exempt
@login_required
def consultar_usuario(request):
    usuarios = Usuario.objects.all()
    return render_to_response("administrador/usuarios/consultar_usuario.html", \
                              {'usuarios_list': usuarios})
    
@csrf_exempt
@login_required
def registrar_usuario(request):
    if request.method == 'POST':
        print "Entro POST"
        print request.POST
        formulario = AdminRegistrarUsuarioForm(request.POST)
        print formulario
        if formulario.is_valid():
            form_usuario = formulario.cleaned_data
            cedula = form_usuario['cedula']
            password = User.objects.make_random_password()
            correo = form_usuario['correo']
            mensaje = 'Nombre de Usuario: '+str(cedula)+' \nclave: '+str(password)
            EmailMessage('Guardabosques Cuenta de Usuario',\
                         mensaje, to = [correo]).send()
            django_user = User.objects.create_user(username=cedula, \
                                            email=correo, password= password)
            django_user.save()
            usuario = Usuario(cedula=form_usuario['cedula'], \
                              correo=form_usuario['correo'])
            ## Se inicializa el tipo del usuario
            tipo_usuario = form_usuario['tipo']
            print "Tipo %s " % tipo_usuario
            if  tipo_usuario == 'Coordinador': # Si el usuario es un coordinador
                usuario.tipo = u'Coordinador'
                usuario.estado = u'Activo'
            else:
                usuario.tipo = u'Estudiante'
                if tipo_usuario == 'Estudiante':
                    usuario.estado = u'Activo'
                else:
                    usuario.estado = u'Inactivo'
            usuario.cedula = form_usuario['cedula']
            usuario.inicializar()
            print usuario.tipo
            print usuario.estado
            usuario.save()
            return HttpResponseRedirect("/administrador/usuarios/registrar_usuario_exito/")
    else:
        formulario = AdminRegistrarUsuarioForm()
    return render_to_response("administrador/usuarios/registrar_usuario.html", \
                              {'form': formulario})    
    
@login_required
def registrar_usuario_exito(request):
    return render_to_response("administrador/usuarios/registrar_usuario_exito.html")


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