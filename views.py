from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required


import datetime

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

