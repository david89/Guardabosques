from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

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
def estudiante_base(request):
    return render_to_response("estudiante/estudiante_base.html")

def html1(request):
    return render_to_response("pages/1.html")
def html2(request):
    return render_to_response("pages/2.html")
