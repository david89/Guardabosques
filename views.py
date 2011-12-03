from django.http import Http404,HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

import datetime

# Vista de prueba
def hello(request):
    return HttpResponse("Hello World")

# Vista de Prueba dinamica
def current_date(request):
    current_date = datetime.datetime.now()
    return render_to_response('base_template.html', locals())



# Vista dinamica que recibe parametros
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

