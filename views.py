# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

#from django.http import Http404,HttpResponse, HttpResponseRedirect
#from django.template.loader import get_template
#from django.template import Context
#from django.views.decorators.csrf import csrf_exempt
#
#
#
#import datetime

##
#  Vista que redirecciona a la vista de administrador o de usuario según sea
#  el caso.
@login_required
def inicio(request):
    if request.user.is_staff:
        return render_to_response("inicio_coordinador.html",
                                  {},
                                  context_instance=RequestContext(request))

    return render_to_response(u'inicio_usuario.html',
                              {},
                              context_instance=RequestContext(request))

