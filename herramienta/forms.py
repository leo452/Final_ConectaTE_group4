# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.admin import widgets
import models
from cuser.middleware import CuserMiddleware

#creacion del formulario de categoria
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria

        fields = ['nombre', 'descripcion']

#creacion del formulario de herramienta
class HerramientaForm(forms.ModelForm):
    class Meta:
        model = models.Herramienta
        fields = ['nombre', 'estado', 'tipo', 'descripcion','licencia', 'usos','enlaces', 'descarga_url','sistema_operativo','version','integracion_lms','informacion', 'documentacion']
        exclude = ['owner']

    def save(self, commit=True):
        instance = super(HerramientaForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance

#creacion del formulario de estado de revision
class RevisioForm(forms.ModelForm):
    class Meta:
        model = models.Revision
        fields = ['nombre', 'descripcion']

#creacion del fomrulario de edicion de herramienta
class HerramientaEdicionForm(forms.ModelForm):
    class Meta:
        model = models.HerramientaEdicion
        fields = ['herramienta','tipo','revision','nombre', 'descripcion','licencia', 'usos','enlaces', 'descarga_url','sistema_operativo','version','integracion_lms','informacion', 'documentacion',  'observacion']
        exclude = ['owner', 'usuarioHerramienta']