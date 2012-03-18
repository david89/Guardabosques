from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt

# Modelos
from database.models import Usuario


from django.contrib.auth.decorators import login_required


import datetime

@csrf_exempt
@login_required
def json_usuarios(request):
    jsonUsuario = serializers.serialize("json", Usuario.objects.all(), fields=('cedula', 'correo'))
    return HttpResponse(jsonUsuario, 'application/javascript')
