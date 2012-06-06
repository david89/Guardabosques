from django import template

register = template.Library()

@register.simple_tag
def total_horas(jornada):
    return jornada.tiempo_de_trabajo().strftime('%H:%M')

@register.simple_tag
def estado(jornada):
    if jornada.estado == 'P':
        return u'Pendiente'
    elif  jornada.estado == 'A':
        return u'Aprobada'
    else:
        return u'Rechazada'
