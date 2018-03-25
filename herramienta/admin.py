# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
import models
import forms
from django.contrib import admin

# Register your models here.
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


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = list_display
    form = forms.CategoriaForm


class HerramientaAdmin(admin.ModelAdmin):
    inlines = [EdicionHerramientaInline]
    list_display = ['owner','nombre', 'descripcion', 'informacion', 'usos', 'enlaces', 'documentacion', 'estado', 'licencia']
    search_fields = ['owner__first_name','owner__last_name','nombre', 'descripcion', 'informacion', 'usos', 'enlaces', 'documentacion', 'estado', 'licencia']
    form = forms.HerramientaForm


class HerramientaEdicionAdmin(admin.ModelAdmin):
    list_display = ['editor','nombre', 'descripcion', 'informacion', 'usos', 'enlaces', 'documentacion', 'licencia']
    search_fields = ['usuarioHerramienta__usuario__first_name', 'usuarioHerramienta__usuario__last_name','nombre', 'descripcion', 'informacion', 'usos', 'enlaces', 'documentacion', 'licencia']
    form = forms.HerramientaEdicionForm


admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Herramienta, HerramientaAdmin)
admin.site.register(models.HerramientaEdicion, HerramientaEdicionAdmin)