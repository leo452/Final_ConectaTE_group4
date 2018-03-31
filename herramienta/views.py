# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from herramienta.models import Herramienta


def home(request):
    lista_herramientas = Herramienta.objects.all()
    context = {'lista_herramientas': lista_herramientas}
    return render(request, 'home.html', context)


def details(request, index=None):
    instance = get_object_or_404(Herramienta, id=index)
    context = {'herramienta': instance}
    return render(request, 'detalleherramienta.html', context)
