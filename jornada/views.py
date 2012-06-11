from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.forms.models import inlineformset_factory
from django.views.generic import DetailView

from Guardabosques.jornada.models import Jornada, ConstituidaPor
from Guardabosques.jornada.forms import FormularioJornada, FormularioActividad,\
                                        BaseActividadFormSet
from Guardabosques.usuario.models import Perfil

@staff_member_required
def jornadas_pendientes(request):
    """
    Lista las jornadas pertenecientes de los usuarios.
    """
    plantilla = u'jornada/jornadas_pendientes.html'
    jornadas = Jornada.objects.filter(estado=u'P')
    if request.method == 'POST':
        for jornada in jornadas:
            jornada.estado =  request.POST.get('%s' % jornada.pk)
            jornada.save()
    return render_to_response(plantilla, {u'jornadas' : jornadas},
                              context_instance=RequestContext(request))


class DetallesJornada(DetailView):
    context_object_name = u'jornada'
    model = Jornada

    def get_context_data(self, **kwargs):
        context = super(DetallesJornada, self).get_context_data(**kwargs)
        if self.request.user.is_staff:
            context[u'plantilla_base'] = u'inicio_coordinador.html'
        else:
            context[u'plantilla_base'] = u'inicio_estudiante.html'
        context[u'horas_totales'] = context[u'jornada'].tiempo_de_trabajo()
        return context

@login_required
def descripcion_jornada(request, identificador):
    plantilla = u'jornada/descripcion_jornada.html'
    j = Jornada.objects.get(id=identificador)
    detalles = ConstituidaPor.objects.filter(jornada=j)
    if request.user.is_staff:
        plantilla_base = u'inicio_coordinador.html'
    else:
        plantilla_base = u'inicio_estudiante.html'
    print plantilla_base
    ctx = {u'detalles' : detalles, u'plantilla_base' : plantilla_base}
    return render_to_response(plantilla, ctx,
                              context_instance=RequestContext(request))

@login_required
def administrar_jornadas(request):
    """
    Lista las jornadas que posee el usuario.
    """
    if request.user.is_staff:
        plantilla = u'jornada/jornadas_pendientes.html'
        jornadas = Jornada.objects.filter(estado='P')
        return render(request, plantilla, {u'jornadas':jornadas})
    else:
        plantilla = u'jornada/jornadas_de_trabajo.html'
        perfil_usuario = Perfil.objects.get(usuario__id=request.user.pk)
        jornadas = Jornada.objects.filter(perfil__id=perfil_usuario.pk)
        return render(request, plantilla,
                      {u'jornadas' : jornadas, u'tipo' : "pendiente"})

@login_required
def agregar_jornada(request, jornada_pk=None):
    """ Agregar una nueva jornada """
    plantilla = u'jornada/agregar_jornada.html'
    if not jornada_pk:
        jornada = Jornada()
    else:
        jornada = Jornada.objects.get(pk=jornada_pk)
    ConjuntoActividades = inlineformset_factory(Jornada, ConstituidaPor, \
                                                extra=1, \
                                                formset=BaseActividadFormSet, \
                                                can_delete=False)
    if request.POST:

        form_jornada = FormularioJornada(request.POST)
        form_actividades = ConjuntoActividades(request.POST)

        if form_jornada.is_valid():
            jornada = form_jornada.save(commit=False)
            perfil = Perfil.objects.get(usuario=request.user.pk)
            jornada.perfil = perfil
            form_actividades = ConjuntoActividades(request.POST,
                                                   instance=jornada)

            if form_actividades.is_valid():
                jornada.save()
                form_actividades.save()
                return redirect(u'administrar_jornadas')

    else:
        form_jornada = FormularioJornada(instance=jornada)
        form_actividades = ConjuntoActividades(instance=jornada)
    return render_to_response(plantilla,
                              {u'form_jornada' : form_jornada,
                               u'form_actividades' : form_actividades},
                              context_instance=RequestContext(request))

@login_required
def eliminar_jornada(request, jornada_pk):
    """ Elimina una jornada pendiente """
    Jornada.objects.get(pk=jornada_pk).delete()
    return redirect(u'administrar_jornadas')

