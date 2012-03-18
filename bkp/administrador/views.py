from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

## Vistas de la seccion de administrador
@login_required
def administrador_base(request):
    return render_to_response("administrador/administrador_base.html")
administrador_base = staff_member_required(administrador_base)

