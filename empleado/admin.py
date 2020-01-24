# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Empleado

# Register your models here.
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_show = [
        'nombre'
    ]