from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# Decoradores
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



## Vistas de la seccion de administrador
@csrf_exempt
@login_required
def estudiante_base(request):
    return render_to_response("estudiante/estudiante_base.html")