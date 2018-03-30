# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from herramienta.models import Herramienta


def home(request):
    lista_herramientas = Herramienta.objects.all()
    context = {'lista_herramientas': lista_herramientas}
    return render(request, 'home.html', context)
