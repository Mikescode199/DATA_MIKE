# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#SE CAMBIÓ DE NOMBRE 
class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    #SE MODIFICÓ
    apellido_materno3 = models.CharField(max_length=20)
    #SE AGREGÓ
    lenguage_programacion = models.CharField(max_length=20)
    profesion = models.CharField(max_length=20)
    telefono = models.IntegerField()
    edad = models.IntegerField()

