# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Actividad(models.Model):
    nombre = models.CharField(u'Nombre', max_length=50, unique=True)
    descripcion = models.TextField(u'Descripción', blank=True, null=True)
    obj1 = models.BooleanField()
    obj2 = models.BooleanField()
    obj3 = models.BooleanField()
    obj4 = models.BooleanField()
    obj5 = models.BooleanField()

    def __unicode__(self):
        return self.nombre
