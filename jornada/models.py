import datetime
from actividad.models import Actividad
from usuario.models import Perfil
from django.db import models

ESTADO_JORNADA = (
    (u'P', u'Pendiente'),
    (u'A', u'Aprobada'),
    (u'R', u'Rechazada'),
)

class ConstituidaPor(models.Model):
    jornada = models.ForeignKey(u'Jornada')
    actividad = models.ForeignKey(Actividad)
    descripcion = models.TextField(null=True, blank=True)
    class Meta:
        db_table = u'constituida_por'

class Jornada(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    perfil = models.ForeignKey(Perfil)
    actividades = models.ManyToManyField(Actividad,
                                         through=u'ConstituidaPor')
    estado = models.CharField(choices=ESTADO_JORNADA, max_length=1, default=u'P')

    def tiempo_de_trabajo(self):
        """Horas y minutos invertidos en la jornada"""
        s1 = self.hora_inicio.strftime('%H:%M')
        s2 = self.hora_fin.strftime('%H:%M')
        fmt = '%H:%M'
        td = datetime.datetime.strptime(s2, fmt) - datetime.datetime.strptime(s1, fmt)
        return datetime.time(td.seconds/3600, (td.seconds/60)%60)

    def save(self, *args, **kwargs):
        if self.hora_fin < self.hora_inicio:
            raise ValidationError(u'La hora inicial es mayor que la hora'\
                                  u'final')
        super(Jornada, self).save(*args, **kwargs)
