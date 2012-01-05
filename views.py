from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

# Modelos
from database.models import Usuario

# Formularios
from formularios.formularios import AdminRegistrarUsuarioForm

# Usuarios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required


import datetime

# Vista de prueba
def hello(request):
    return HttpResponse("Hello World")

# Vista de Prueba dinamica
def current_date(request):
    current_date = datetime.datetime.now()
    return render_to_response('base_template.html', locals())


## Vista que redirecciona a la vista de admin o de usuario segun sea el caso
@login_required
def principal(request):
    if request.user.is_staff:
        return HttpResponseRedirect("/administrador/")
    else:
        return HttpResponseRedirect("/estudiante/")


## Vistas de la seccion de administrador
@login_required
def administrador_base(request):
    return render_to_response("administrador/administrador_base.html")

@csrf_exempt
@login_required
def administrador_registrar_usuario(request):
    if request.method == 'POST':
        formulario = AdminRegistrarUsuarioForm(request.POST)
        if formulario.is_valid():
            form_usuario = formulario.cleaned_data
            django_user = User.objects.create_user(username = form_usuario['cedula'],\
                                            email = form_usuario['correo'],\
                                         password = User.objects.make_random_password())
            django_user.save()
            usuario = Usuario(cedula = form_usuario['cedula'],\
                              correo = form_usuario['correo'])
            ## Se inicializa el tipo del usuario
            tipo_usuario = form_usuario['tipo']
            print "Tipo %s " % tipo_usuario
            if  tipo_usuario == 'coord': # Si el usuario es un coordinador
                usuario.tipo = u'Coordinador'
                usuario.estado = u'Activo'
            else:
                usuario.tipo = u'Estudiante'
                if tipo_usuario == 'est_act':
                    usuario.estado = u'Activo'
                else:
                    usuario.estado = u'Inactivo'
            usuario.cedula = form_usuario['cedula']
            usuario.inicializar()
            print usuario.tipo
            print usuario.estado
            usuario.save()
            return HttpResponseRedirect("/administrador/registrar_usuario_exito/")
    else:
        formulario = AdminRegistrarUsuarioForm()
    return render_to_response("administrador/administrador_registrar_usuario.html",\
                              {'formulario': formulario})
@login_required
def administrador_registrar_usuario_exito(request):
    return render_to_response("administrador/administrador_registrar_usuario_exito.html")

## Vistas de la seccion de administrador
@login_required
def estudiante_base(request):
    return render_to_response("estudiante/estudiante_base.html")

