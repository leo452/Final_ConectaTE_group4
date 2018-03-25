# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.admin import widgets
import models
from cuser.middleware import CuserMiddleware


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ['nombre', 'descripcion']


class HerramientaForm(forms.ModelForm):
    class Meta:
        model = models.Herramienta
        fields = ['nombre', 'descripcion', 'informacion', 'usos', 'enlaces', 'documentacion', 'estado', 'licencia', 'descarga_url', 'tipo']
        exclude = ['owner']

    def save(self, commit=True):
        instance = super(HerramientaForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance


class RevisioForm(forms.ModelForm):
    class Meta:
        model = models.Revision
        fields = ['nombre', 'descripcion']


class HerramientaEdicionForm(forms.ModelForm):
    class Meta:
        model = models.HerramientaEdicion
        fields = ['herramienta','nombre', 'descripcion', 'informacion', 'usos', 'enlaces', 'documentacion', 'licencia', 'descarga_url', 'tipo']
        exclude = ['owner', 'usuarioHerramienta']