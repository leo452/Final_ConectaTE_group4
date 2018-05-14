# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.decorators import method_decorator
from django.views import View

import models
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from forms import CategoriaForm, RevisioForm, HerramientaForm, HerramientaEdicionForm, ImporterForm
from django.views.generic import ListView
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from herramienta.importer import CSVImporterTool
from herramienta.models import Herramienta, HerramientaPorAprobar
from herramienta.templatetags import filters
from herramienta import EmailHandler
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
import usuario.models

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
            mensaje = {"mensaje": "Categoría agregada con Éxito!"}
            return HttpResponse(json.dumps({"mensaje": mensaje}), status=200,
                                content_type='application/json')
            #messages.success(request, 'Categoría agregada con Éxito!')
            #return redirect('home')

        erros = form.errors.items()
        return HttpResponse(json.dumps(erros), status=400,
                            content_type='application/json')
    mensaje = "Metodo no permitido"
    return HttpResponse(json.dumps({"error": mensaje}),status=404,
                        content_type='application/json')


#
def getCategoria(request):
    if request.method == "GET":
        id = request.GET.get('id')
        if id:
            categoria = models.Categoria.objects.get(id=id)
        else:
            categoria = models.Categoria.objects.all()

        data = serializers.serialize('json', categoria)
        return HttpResponse(data, status=200,
                            content_type='application/json')
    mensaje = "Metodo no permitido"
    return HttpResponse(json.dumps({"error": mensaje}), status=404,
                        content_type='application/json')


def in_admin_group(user):
    group = Group.objects.get(name="Administrador")
    return True if group in user.groups.all() else False


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
            mensaje = {"mensaje": "Estado de Revisión agregado con Éxito!"}
            return HttpResponse(json.dumps({"mensaje": mensaje}), status=200,
                                content_type='application/json')
            #messages.success(request, 'Estado de Revisión agregado con Éxito!')
            #return redirect('home')

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
            messages.success(request, 'Herramienta agregada con Éxito!')
            #return redirect('home')
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

    if filters.is_herramienta_owner(request.user, herramienta) or in_admin_group(request.user):
        if request.method == "POST":
            form = HerramientaForm(request.POST, instance=herramienta)
            if form.is_valid():
                form.save()
                messages.success(request, 'Herramienta editada con Éxito!')
                #return redirect('home')
                mensaje = {"mensaje": "edicion de herramienta exitoso"}
                return HttpResponse(json.dumps(mensaje), status=200,
                                    content_type='application/json')
            erros = form.errors.items()
            return HttpResponse(json.dumps(erros), status=400,
                                content_type='application/json')
        mensaje = "Metodo no permitido"
        return HttpResponse(json.dumps({"mensaje": mensaje}),status=404,
                            content_type='application/json')

    else:
        return redirect('home')


# esta vista se llama usando la url herramienta/delete/#, se encarga de procesar la peticion tipo DELETE
# y elimina la herramienta que es pasada como parametro
# recive un parametro que es el id de la herramienta a eliminar
# retorna un JSON que indica el resultado de la operacion
@csrf_exempt
def deleteHerramienta(request, id):
    try:
        herramienta = models.Herramienta.objects.get(id=id)
    except ObjectDoesNotExist:
        mensaje = "La Herramienta No Existe"
        return HttpResponse(json.dumps({"error": mensaje}), status=404,
                            content_type='application/json')
    if request.method == "DELETE":
        herramienta.delete()
        mensaje = {"mensaje": "Herramienta eliminada"}
        return HttpResponse(json.dumps(mensaje), status=200, content_type='application/json')
    return redirect('home')


def editHerramientaField(request, id):
    try:
        herramienta = models.Herramienta.objects.get(id=id)
    except ObjectDoesNotExist:
        messages.error(request, 'Herramienta no encontrada')
        return redirect('home')

    if not filters.has_group(request.user, "Administrador"):
        if herramienta.estado == 0 and filters.is_herramienta_owner(request.user, herramienta):
            herramienta.estado = 1
            herramienta.save()

            miembros = User.objects.filter(groups__name="MiembroGTI").exclude(username=request.user.username)
            EmailHandler.send_email_miembro(miembros, request.user, herramienta)

        elif herramienta.estado == 1:
            herramienta.estado = 0
            herramienta.owner = request.user
            herramienta.save()

        if herramienta.estado == 0:
            text = "Borrador"
        else:
            text = "En Revisión"

        messages.success(request, '¡La Herramienta ahora está en estado ' + text + '!')

        # TODO: Add tool to the on revision table.

        return redirect('tool_detail', index=herramienta.id)
    else:
        return redirect('home')


def addHerramientaParaPublicacion (request, id):
    try:
        herramienta = models.Herramienta.objects.get(id=id)
    except ObjectDoesNotExist:
        messages.error(request, 'Herramienta no encontrada')
        return redirect('home')

    if not filters.is_herramienta_owner(request.user, herramienta) and not filters.has_group(request.user, "Administrador"):
        list_revisiones = HerramientaPorAprobar.objects.filter(herramienta_id=herramienta.id)

        for revision in list_revisiones:
            if revision.owner.username == request.user.username:
                messages.error(request, 'Herramienta ya ha sido postulada por ti')
                return redirect('tool_detail', id)

        HerramientaPorAprobar.objects.create(herramienta=herramienta, owner=request.user)

        messages.success(request, 'Herramienta Postulada Correctamente')
        return redirect('tool_detail', id)

    messages.error(request, 'Error de Permisos')
    return redirect('tool_detail', id)


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
            messages.success(request, 'Revision de Herramienta creada con Éxito!')
            # return redirect('home')
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

@user_passes_test(in_admin_group)
def addCategoriaView(request):
    return render(request,'herramienta/add_categoria.html',{"form": CategoriaForm()})

@user_passes_test(in_admin_group)
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

    if filters.is_herramienta_owner(request.user, edicion) or in_admin_group(request.user):
        url = "/herramienta/api/herramientas/form/%d/" % (int(id))
        return render(request,'herramienta/add_herramienta.html',{"form": HerramientaForm(instance=edicion), "url":url})
    else:
        mensaje = "<h1>No tiene acceso a esta herramienta</h1>"
        return HttpResponseNotFound(mensaje)


#vista de ediciones de herramienta

@user_passes_test(in_admin_group)
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


@user_passes_test(in_admin_group)
def addRevisionEstadoView(request):
    return render(request,'herramienta/add_estado_revision.html',{"form": RevisioForm()})

#metodo encargado de dirigir al home y suministrarle la lista de herramientas respectiva segun los filtros
def home(request):
    lista_herramientas = Herramienta.objects.all()
    if filters.has_group(request.user, "MiembroGTI"):
        ownTools = lista_herramientas.filter(estado=0, owner=request.user)
        lista_herramientas = lista_herramientas.exclude(estado=0)
        lista_herramientas = lista_herramientas | ownTools
    elif filters.has_group(request.user, "ConectaTE"):
        lista_herramientas = lista_herramientas.exclude(estado=0)
    elif not filters.has_group(request.user, "Administrador"):
        lista_herramientas = lista_herramientas.filter(estado=2)

    #validar filtro
    categoria = request.GET.get('categoria',False)
    if categoria:
        cat =int(categoria)
        lista_herramientas = lista_herramientas.filter(tipo=cat,estado=1)
    sistema_operativo = request.GET.get('sistema_operativo', False)
    if sistema_operativo:
        lista_herramientas = lista_herramientas.filter(sistema_operativo__icontains=sistema_operativo)
    tipo_licencia = request.GET.get('tipo_licencia', False)
    if tipo_licencia:
        lista_herramientas = lista_herramientas.filter(licencia__icontains=tipo_licencia)
    uso= request.GET.get('uso',False)
    if uso:
        lista_herramientas=lista_herramientas.filter(usos__icontains=uso, estado=1)
    context = {'lista_herramientas': lista_herramientas}
    return render(request, 'home.html', context)


def details(request, index=None):
    instance = get_object_or_404(Herramienta, id=index)

    if (filters.has_group(request.user, "Administrador") or instance.estado == 2 or
    (filters.has_group(request.user, "MiembroGTI") and instance.estado == 1) or
    (filters.has_group(request.user, "ConectaTE") and instance.estado == 1) or
    (filters.has_group(request.user, "MiembroGTI") and instance.estado == 0 and instance.owner == request.user)):
        context = {'herramienta': instance}
        return render(request, 'detalleherramienta.html', context)
    else:
        return redirect('home')


def lista_herramientas_por_publicar (request):
    if(filters.has_group(request.user, "Administrador")):
        lista_postulaciones = HerramientaPorAprobar.objects.all()

        context = {'lista_postulaciones': lista_postulaciones}
        return render(request, 'herramienta/lista_herramientas_publicacion.html', context)
    else:
        return redirect('home')

def lista_postulaciones_aceptar (request, index=None):
    try:
        postulacion = models.HerramientaPorAprobar.objects.get(id=index)
        herramienta = models.Herramienta.objects.get(id=postulacion.herramienta.id)
    except ObjectDoesNotExist:
        mensaje = "<h1>Esta herramienta no existe</h1>"
        return HttpResponseNotFound(mensaje)

    if filters.has_group(request.user, "Administrador"):
        herramienta.estado = 2
        herramienta.save()

        herramientas_por_borrar = models.HerramientaPorAprobar.objects.filter(herramienta_id=herramienta.id)
        for current_postulacion in herramientas_por_borrar:
            current_postulacion.delete()

        return redirect('tool_detail', index=herramienta.id)
    else:
        return redirect('home')

def lista_postulaciones_rechazar (request, index=None):
    try:
        postulacion = models.HerramientaPorAprobar.objects.get(id=index)
        herramienta = models.Herramienta.objects.get(id=postulacion.herramienta.id)
    except ObjectDoesNotExist:
        mensaje = "<h1>Esta herramienta no existe</h1>"
        return HttpResponseNotFound(mensaje)

    if filters.has_group(request.user, "Administrador"):
        herramientas_por_borrar = models.HerramientaPorAprobar.objects.filter(herramienta_id=herramienta.id)
        for current_postulacion in herramientas_por_borrar:
            current_postulacion.delete()

        return redirect('tool_detail', index=herramienta.id)
    else:
        return redirect('home')


def reporteHerramientas(request):
    herramienta_list = models.Herramienta.objects.all()
    paginator = Paginator(herramienta_list, 10)

    page = request.GET.get('page')
    try:
        herramientas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        herramientas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        herramientas = paginator.page(paginator.num_pages)

    ret = []
    for obj in herramientas:
        h_nombre = obj.nombre
        h_fecha = obj.creacion
        edicion  = models.HerramientaEdicion.objects.filter(herramienta=obj.id).order_by('-creacion')[0]
        e_fecha = edicion.creacion
        u = obj.owner
        u_nombre = u.username
        n_ediciones = models.HerramientaEdicion.objects.filter(herramienta=obj.id).count()
        n_tutorial = models.Tutorial.objects.filter(herramienta=obj).count()
        n_ejemplo = models.Ejemplo.objects.filter(herramienta=obj).count()

        ret.append({'herramienta': h_nombre, 'creado': h_fecha, 'edicion': e_fecha, 'usuario': u_nombre,
                    'ediciones': n_ediciones, 'ejemplos': n_ejemplo, 'tutoriales': n_tutorial,
                    'herramientaid': obj.id})

    return render(request, 'herramienta/reporte_herramienta.html', {'lista': ret, 'herramientas': herramientas})


class SaveImporter(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.POST.get('data', '[]'))
        if data:
            for y in data:
                fields = {}
                for key, value in y.items():
                    if value != '':
                        fields.update({key:value})
                if fields:
                    try:
                        del fields['row']
                    except KeyError:
                        pass
                    herrami = models.Herramienta.objects.filter(nombre=fields['nombre'])
                    if herrami:
                        herrami.update(**fields)
                    else:
                        models.Herramienta.objects.create(**fields)
            return HttpResponse(json.dumps({"mensaje": "Actualizacion exitosa", "respuesta": True}),
                                content_type='application/json', status=201)
        return HttpResponse(json.dumps({"mensaje": "Error en el envio del archivo", "respuesta":False}), content_type='application/json', status=201)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SaveImporter, self).dispatch(request, args, kwargs)



class Importer(LoginRequiredMixin, View):
    form_class = ImporterForm
    success_url = '/herramientas/importer'
    template_name = 'herramienta/importer.html'
    importer = CSVImporterTool

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file_user = models.FileUser(file=request.FILES['file'])
            file_user.save()
            impor = self.importer(source=file_user.file, id_file=file_user.id)
            if impor.validar_columnas():
                impor.is_valid()
                datos = impor.save()
                mensaje = {"mensaje": file_user.id, "respuesta":True, "data": datos}
                return HttpResponse(json.dumps(mensaje), content_type='application/json', status=201)
            else:
                mensaje = {"mensaje": "La plantilla no tiene el numero de campos requeridos.", "respuesta": False}
                return HttpResponse(json.dumps(mensaje), content_type='application/json', status=201)
        return HttpResponse(json.dumps(form.errors.as_json()), content_type='application/json', status=201)