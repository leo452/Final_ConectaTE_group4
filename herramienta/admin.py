# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
import models
import forms
from django.contrib import admin

# Register your models here.
#formularios de edicion de herramienta en listado de tabla
class EdicionHerramientaInline(admin.TabularInline):
    model = models.HerramientaEdicion
    extra = 0
    show_change_link = True
    form = forms.HerramientaEdicionForm
    can_delete = False

    def get_readonly_fields(self, request, obj=None):
        # make all fields readonly
        readonly_fields = list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))
        if 'is_submitted' in readonly_fields:
            readonly_fields.remove('is_submitted')
        return readonly_fields


#fomrulario de categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = list_display
    form = forms.CategoriaForm


#formulario de Herramientas por Aprobar
class HerramientaPorAprobarAdmin(admin.ModelAdmin):
    list_display = ['herramienta', 'owner']
    search_fields = list_display


#formulario para los estados de revision
class RevisionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = list_display
    form = forms.RevisioForm


#formulario para la herramienta
class HerramientaAdmin(admin.ModelAdmin):
    inlines = [EdicionHerramientaInline]
    list_display = ['owner','nombre', 'descripcion', 'informacion', 'usos', 'enlaces', 'documentacion', 'estado', 'licencia']
    search_fields = ['owner__first_name','owner__last_name','nombre', 'descripcion', 'informacion', 'usos', 'enlaces', 'documentacion', 'estado', 'licencia']
    form = forms.HerramientaForm


#formulario para edicion de herramienta
class HerramientaEdicionAdmin(admin.ModelAdmin):
    list_display = ['editor','nombre', 'descripcion', 'informacion', 'usos', 'enlaces', 'documentacion', 'licencia']
    search_fields = ['usuarioHerramienta__usuario__first_name', 'usuarioHerramienta__usuario__last_name','nombre', 'descripcion', 'informacion', 'usos', 'enlaces', 'documentacion', 'licencia']
    form = forms.HerramientaEdicionForm


#registro de los formularios en django admin y para usarlos en las vistas
admin.site.register(models.Revision, RevisionAdmin)
admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Herramienta, HerramientaAdmin)
admin.site.register(models.HerramientaEdicion, HerramientaEdicionAdmin)
admin.site.register(models.FileUser)
admin.site.register(models.HerramientaPorAprobar, HerramientaPorAprobarAdmin)
