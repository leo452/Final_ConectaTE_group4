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



class ImporterForm(forms.Form):
    file = forms.FileField()
    class Meta:
        model = models.FileUser
        fields = ['file']
    #end class

    def clean(self):
        clean_data = super(ImporterForm, self).clean()
        print 'Este es archivo q existe  - >',clean_data
        if clean_data.get('file'):
            path = str(clean_data.get('file')).split('.')
            if len(path)>1:
                if path[1] != 'csv':
                    self.add_error('file', 'El archivo debe ser de la extencion csv.')
            else:
                self.add_error('file', 'El archivo es requerido con extencion csv.')

