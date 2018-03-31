# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import models
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from forms import CategoriaForm, RevisioForm,HerramientaForm,HerramientaEdicionForm
from django.shortcuts import render
from django.views.generic import ListView
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from herramienta.models import Herramienta

# Create your views here.
#API PARA CATERGORIAS
class AJAXListMixin(object):

    def dispatch(self, request, *args, **kwargs):
        return super(AJAXListMixin, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(AJAXListMixin, self).get_queryset()


    def get(self, request, *args, **kwargs):
        return HttpResponse(serializers.serialize('json', self.get_queryset()))


@csrf_exempt
def addCategoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = {"mensaje": "Guardado exitoso"}
            return HttpResponse(json.dumps({"mensaje": "Guardado exitoso"}),status=200,
                                content_type='application/json')

        erros = form.errors.items()
        return HttpResponse(json.dumps(erros), status=400,
                            content_type='application/json')
    mensaje = "Metodo no permitido"
    return HttpResponse(json.dumps({"error": mensaje}),status=404,
                        content_type='application/json')

@csrf_exempt
def editCategoria(request, id):
    try:
        categoria = models.Categoria.objects.get(id=id)
    except ObjectDoesNotExist:
        mensaje = "Esta categoria no existe"
        return HttpResponse(json.dumps({"error": mensaje}), status=404,
                            content_type='application/json')

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            mensaje = {"mensaje": "Guardado exitoso"}
            return HttpResponse(json.dumps({"mensaje": mensaje}), status=200,
                                content_type='application/json')
        erros = form.errors.items()
        return HttpResponse(json.dumps(erros), status=400,
                            content_type='application/json')
    mensaje = "Metodo no permitido"
    return HttpResponse(json.dumps({"mensaje": mensaje}),status=404,
                        content_type='application/json')


class ListCategorias(AJAXListMixin, ListView):
    model = models.Categoria

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        querysert = super(AJAXListMixin, self).get_queryset()
        return querysert.filter(nombre__icontains=q)

#API PARA REVISIONES

@csrf_exempt
def addRevision(request):
    if request.method == "POST":
        form = RevisioForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = {"mensaje": "Guardado exitoso"}
            return HttpResponse(json.dumps({"mensaje": "Guardado exitoso"}),status=200,
                                content_type='application/json')

        erros = form.errors.items()
        return HttpResponse(json.dumps(erros), status=400,
                            content_type='application/json')
    mensaje = "Metodo no permitido"
    return HttpResponse(json.dumps({"error": mensaje}),status=404,
                        content_type='application/json')

@csrf_exempt
def editRevision(request, id):
    try:
        revision = models.Revision.objects.get(id=id)
    except ObjectDoesNotExist:
        mensaje = "Esta revision no existe"
        return HttpResponse(json.dumps({"error": mensaje}), status=404,
                            content_type='application/json')

    if request.method == "POST":
        form = RevisioForm(request.POST, instance=revision)
        if form.is_valid():
            form.save()
            mensaje = {"mensaje": "Guardado exitoso"}
            return HttpResponse(json.dumps({"mensaje": mensaje}), status=200,
                                content_type='application/json')
        erros = form.errors.items()
        return HttpResponse(json.dumps(erros), status=400,
                            content_type='application/json')
    mensaje = "Metodo no permitido"
    return HttpResponse(json.dumps({"mensaje": mensaje}),status=404,
                        content_type='application/json')


class ListRevisiones(AJAXListMixin, ListView):
    model = models.Revision

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        querysert = super(AJAXListMixin, self).get_queryset()
        return querysert.filter(nombre__icontains=q)

#API DE HERRAMIENTAS

@csrf_exempt
def addHerramienta(request):
    if request.method == "POST":
        form = HerramientaForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = {"mensaje": "Guardado exitoso"}
            return HttpResponse(json.dumps({"mensaje": "Guardado exitoso"}),status=200,
                                content_type='application/json')

        erros = form.errors.items()
        return HttpResponse(json.dumps(erros), status=400,
                            content_type='application/json')
    mensaje = "Metodo no permitido"
    return HttpResponse(json.dumps({"error": mensaje}),status=404,
                        content_type='application/json')

@csrf_exempt
def editHerramienta(request, id):
    try:
        herramienta = models.Herramienta.objects.get(id=id)
    except ObjectDoesNotExist:
        mensaje = "Esta herramienta no existe"
        return HttpResponse(json.dumps({"error": mensaje}), status=404,
                            content_type='application/json')

    if request.method == "POST":
        form = HerramientaForm(request.POST, instance=herramienta)
        if form.is_valid():
            form.save()
            mensaje = {"mensaje": "edicion de herramienta exitoso"}
            return HttpResponse(json.dumps(mensaje), status=200,
                                content_type='application/json')
        erros = form.errors.items()
        return HttpResponse(json.dumps(erros), status=400,
                            content_type='application/json')
    mensaje = "Metodo no permitido"
    return HttpResponse(json.dumps({"mensaje": mensaje}),status=404,
                        content_type='application/json')


class ListHerramienta(AJAXListMixin, ListView):
    model = models.Herramienta

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        querysert = super(AJAXListMixin, self).get_queryset()
        return querysert.filter(nombre__icontains=q)

#API PARA EDICION DE HERRAMIENTAS
@csrf_exempt
def addHerramientaEdicion(request):
    if request.method == "POST":
        form = HerramientaEdicionForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = {"mensaje": "Guardado exitoso"}
            return HttpResponse(json.dumps({"mensaje": "Guardado exitoso"}),status=200,
                                content_type='application/json')

        erros = form.errors.items()
        return HttpResponse(json.dumps(erros), status=400,
                            content_type='application/json')
    mensaje = "Metodo no permitido"
    return HttpResponse(json.dumps({"error": mensaje}),status=404,
                        content_type='application/json')

@csrf_exempt
def editHerramientaEdicion(request, id):
    try:
        edicion = models.HerramientaEdicion.objects.get(id=id)
    except ObjectDoesNotExist:
        mensaje = "Esta herramienta no existe"
        return HttpResponse(json.dumps({"error": mensaje}), status=404,
                            content_type='application/json')

    if request.method == "POST":
        form = HerramientaEdicionForm(request.POST, instance=edicion)
        if form.is_valid():
            form.save()
            mensaje = {"mensaje": "edicion de herramienta exitoso"}
            return HttpResponse(json.dumps(mensaje), status=200,
                                content_type='application/json')
        erros = form.errors.items()
        return HttpResponse(json.dumps(erros), status=400,
                            content_type='application/json')
    mensaje = "Metodo no permitido"
    return HttpResponse(json.dumps({"mensaje": mensaje}),status=404,
                        content_type='application/json')


class ListHerramientaEdicion(AJAXListMixin, ListView):
    model = models.HerramientaEdicion

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        querysert = super(AJAXListMixin, self).get_queryset()
        return querysert.filter(nombre__icontains=q)

#vistas de herramientas

def addCategoriaView(request):
    return render(request,'herramienta/add_categoria.html',{"form": CategoriaForm()})


def listHerramienta(request):
    herramienta_list = models.Herramienta.objects.all()
    paginator = Paginator(herramienta_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        herramientas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        herramientas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        herramientas = paginator.page(paginator.num_pages)

    return render(request, 'herramienta/lista_herramientas.html', {'herramientas': herramientas})


def addHerramientaView(request):
    url = "/herramienta/api/herramientas/form/"
    return render(request,'herramienta/add_herramienta.html',{"form": HerramientaForm(), "url": url})

def editHerramientaView(request, id):
    try:
        edicion = models.Herramienta.objects.get(id=id)
    except ObjectDoesNotExist:
        mensaje = "<h1>Esta herramienta no existe</h1>"
        return HttpResponseNotFound(mensaje)

    url = "/herramienta/api/herramientas/form/%d/" % (int(id))
    return render(request,'herramienta/add_herramienta.html',{"form": HerramientaForm(instance=edicion), "url":url})


#vista de ediciones de herramienta

def listRevisiones(request):
    revisiones_list = models.HerramientaEdicion.objects.all()
    paginator = Paginator(revisiones_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        revisiones = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        revisiones = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        revisiones = paginator.page(paginator.num_pages)

    return render(request, 'herramienta/lista_ediciones.html', {'revisiones': revisiones})


def addRevisionView(request):
    url = "/herramienta/api/edicion/form/"
    return render(request,'herramienta/add_edicion_herramienta.html',{"form": HerramientaEdicionForm(), "url":url})

#def editRevisionView(request, id):
 #   try:
  #      edicion = models.HerramientaEdicion.objects.get(id=id)
   # except ObjectDoesNotExist:
    #    mensaje = "<h1>Esta edicion no existe</h1>"
     #   return HttpResponseNotFound(mensaje)

    #url = "/herramienta/api/edicion/form/%d/" % (int(id))
    #return render(request,'herramienta/add_edicion_herramienta.html',{"form": HerramientaEdicionForm(instance=edicion), "url":url})



def addRevisionEstadoView(request):
    return render(request,'herramienta/add_estado_revision.html',{"form": RevisioForm()})

def home(request):
    lista_herramientas = Herramienta.objects.all()
    context = {'lista_herramientas': lista_herramientas}
    return render(request, 'home.html', context)


def details(request, index=None):
    instance = get_object_or_404(Herramienta, id=index)
    context = {'herramienta': instance}
    return render(request, 'detalleherramienta.html', context)
