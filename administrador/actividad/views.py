from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# Decoradores
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Modelos
from database.models import Actividad

# Formularios
from formularios.formularios import AdminRegistrarActividadForm

@login_required
def gestionar_actividad(request):
    return render_to_response("administrador/actividad/gestionar_actividad.html")

@csrf_exempt
@login_required
def consultar_actividad(request):
    actividad = Actividad.objects.all()
    return render_to_response("administrador/actividad/consultar_actividad.html", \
                              {'actividad_list': actividad})
    
@csrf_exempt
@login_required
def registrar_actividad(request):
    if request.method == 'POST':
        formulario = AdminRegistrarActividadForm(request.POST)
        if formulario.is_valid():
            form_actividad = formulario.cleaned_data
            formulario.save()
            return HttpResponseRedirect("/administrador/actividad/registrar_actividad_exito/")
    else:
        formulario = AdminRegistrarActividadForm()
    return render_to_response("administrador/actividad/registrar_actividad.html", \
                              {'form': formulario})    

@login_required
def registrar_actividad_exito(request):
    return render_to_response("administrador/actividad/registrar_actividad_exito.html")

@login_required
def eliminar_actividad(request, nombre):
    try:
        actividad = Actividad.objects.get(nombre=nombre)
    except Actividad.DoesNotExist:
        return render_to_response("administrador/actividad/eliminar_actividad.html",\
                                  {'error':nombre, 'tipo' : 'Uactividad'})
    else:
        actividad.delete()
        return render_to_response("administrador/actividad/eliminar_actividad.html")
    
@csrf_exempt
@login_required
def modificar_actividad(request,nombre):
    if request.method == 'POST':
        if 'nombre' in request.POST:
            nombre = request.POST['nombre']
            
        else:
            return render_to_response("administrador/actividad/modificar_actividad_exito.html",\
                                      {'error':nombre, 'tipo' : 'actividad'})
        try:
            actividad = Actividad.objects.get(nombre=nombre)
        except Actividad.DoesNotExist:
            print "error actividad no eixsteD"
            return render_to_response("administrador/actividad/modificar_actividad_exito.html",\
                                      {'error':nombre, 'tipo' : 'actividad'})
        else:
            formulario = AdminRegistrarActividadForm(request.POST,instance= actividad)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/administrador/actividad/modificar_actividad_exito/")
            else:
                return render_to_response("administrador/actividad/modificar_actividad_exito.html",\
                                              {'error':nombre, 'tipo' : 'DJango USer'})
    else:
        try:
            actividad = Actividad.objects.get(nombre=nombre)
        except actividad.DoesNotExist:
            return render_to_response("administrador/actividad/modificar_actividad.html",\
                                      {'error':nombre, 'tipo' : 'actividad'})
        else:
            formulario = AdminRegistrarActividadForm(instance = actividad)
            return render_to_response("administrador/actividad/modificar_actividad.html", \
                              {'form': formulario}) 
            
@login_required
def modificar_actividad_exito(request):
    return render_to_response("administrador/actividad/modificar_actividad_exito.html")