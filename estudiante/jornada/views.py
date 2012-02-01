from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# Decoradores
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Modelos
from database.models import Jornada, Actividad, ConstituidaPor, Usuario

# Formularios
from formularios.formularios import EstRegistrarJornadaForm

@login_required
def gestionar_jornada(request):
    return render_to_response("estudiante/jornada/gestionar_jornada.html")

@csrf_exempt
@login_required
def consultar_jornada(request):
    jornada = Jornada.objects.all()
    actividad = Actividad.objects.all()
    return render_to_response("estudiante/jornada/consultar_jornada.html", \
                              {'jornada_list': jornada})
    
@csrf_exempt
@login_required
def registrar_jornada(request):
    if request.method == 'POST':
        formulario = EstRegistrarJornadaForm(request.POST)
        print formulario
        if formulario.is_valid():
            form_jornada = formulario.cleaned_data
            u = Usuario.objects.get(cedula=request.user.username)
            jornada = Jornada.objects.create(cedula_usuario = u,
                                   minutos =  form_jornada['minutos'],
                                   fecha = form_jornada['fecha'],
                                   multiplicador = 1.0,
                                   estado='Pendiente')
            print jornada
            for actividad in form_jornada['actividad']:
                act = Actividad.objects.get(nombre=actividad.nombre)
                ConstituidaPor.objects.create(nombre_actividad = act, 
                                              identificador_jornada = jornada)
            return HttpResponseRedirect("/estudiante/jornada/registrar_jornada_exito/")
    else:
        formulario = EstRegistrarJornadaForm()
    return render_to_response("estudiante/jornada/registrar_jornada.html", \
                              {'form': formulario})    

@login_required
def registrar_jornada_exito(request):
    return render_to_response("estudiante/jornada/registrar_jornada_exito.html")

@login_required
def eliminar_jornada(request, nombre):
    try:
        jornada = Jornada.objects.get(nombre=nombre)
    except Jornada.DoesNotExist:
        return render_to_response("estudiante/jornada/eliminar_jornada.html",\
                                  {'error':nombre, 'tipo' : 'Ujornada'})
    else:
        jornada.delete()
        return render_to_response("estudiante/jornada/eliminar_jornada.html")
    
@csrf_exempt
@login_required
def modificar_jornada(request,nombre):
    if request.method == 'POST':
        if 'nombre' in request.POST:
            nombre = request.POST['nombre']
            
        else:
            return render_to_response("estudiante/jornada/modificar_jornada_exito.html",\
                                      {'error':nombre, 'tipo' : 'jornada'})
        try:
            jornada = Jornada.objects.get(nombre=nombre)
        except Jornada.DoesNotExist:
            print "error jornada no eixsteD"
            return render_to_response("estudiante/jornada/modificar_jornada_exito.html",\
                                      {'error':nombre, 'tipo' : 'jornada'})
        else:
            formulario = AdminRegistrarJornadaForm(request.POST,instance= jornada)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/estudiante/jornada/modificar_jornada_exito/")
            else:
                return render_to_response("estudiante/jornada/modificar_jornada_exito.html",\
                                              {'error':nombre, 'tipo' : 'DJango USer'})
    else:
        try:
            jornada = Jornada.objects.get(nombre=nombre)
        except jornada.DoesNotExist:
            return render_to_response("estudiante/jornada/modificar_jornada.html",\
                                      {'error':nombre, 'tipo' : 'jornada'})
        else:
            formulario = AdminRegistrarJornadaForm(instance = jornada)
            return render_to_response("estudiante/jornada/modificar_jornada.html", \
                              {'form': formulario}) 
            
@login_required
def modificar_jornada_exito(request):
    return render_to_response("estudiante/jornada/modificar_jornada_exito.html")