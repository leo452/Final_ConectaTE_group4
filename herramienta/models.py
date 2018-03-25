# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from cuser.fields import CurrentUserField
from django.db import models

# Create your models here.
from django_model_changes import ChangesMixin

from usuario.models import Usuario

class Categoria (models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return '%s'%self.nombre

    def __str__(self):
        return '%s' % self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Herramienta(ChangesMixin, models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.CharField(max_length=1000, null=True, blank=True)
    informacion= models.CharField(max_length=1000, null=True, blank=True)
    usos = models.CharField(max_length=1000, null=True, blank=True)
    enlaces = models.CharField(max_length=1000, null=True, blank=True)
    documentacion = models.CharField(max_length=1000, null=True, blank=True)
    estado=models.IntegerField(choices=((0, 'Borrador'), (1, 'Revisión'), (2, 'Publica')), default=0)
    licencia = models.CharField(max_length=1000, null=True, blank=True) #add
    descarga_url = models.CharField(max_length=1000, null=True, blank=True)#add
    creacion =models.DateField(auto_now_add=True)#add
    tipo= models.ForeignKey(Categoria, null=True, blank=True)#add
    owner= CurrentUserField(add_only=True, related_name="created_mymodels")

    def __unicode__(self):
        return '%s'%self.nombre

    def __str__(self):
        return '%s' % self.nombre

    class Meta:
        verbose_name = 'Herramienta'
        verbose_name_plural = 'Herramientas'


class Revision (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.nombre

    def __str__(self):
        return '%s' % self.nombre

    class Meta:
        verbose_name = 'Revision'
        verbose_name_plural = 'Revisiones'


class HerramientaEdicion(ChangesMixin, models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.CharField(max_length=1000, null=True, blank=True)
    informacion = models.CharField(max_length=1000, null=True, blank=True)
    usos = models.CharField(max_length=1000, null=True, blank=True)
    enlaces = models.CharField(max_length=1000, null=True, blank=True)
    documentacion = models.CharField(max_length=1000, null=True, blank=True)
    licencia = models.CharField(max_length=1000, null=True, blank=True)  # add
    descarga_url = models.CharField(max_length=1000, null=True, blank=True)  # add
    creacion = models.DateField(auto_now_add=True)  # add
    tipo = models.ForeignKey(Categoria, null=True, blank=True)  # add
    usuarioHerramienta= CurrentUserField(add_only=True, related_name='created_edit_model', on_delete=models.CASCADE)
    herramienta=models.ForeignKey(Herramienta)
    revision =  models.ForeignKey(Revision, blank=True, null=True, verbose_name='Estado de revision')
    observacion =  models.CharField(max_length=1000, blank=True, null=True, verbose_name='Observacion')

    def __unicode__(self):
        return '%s' % self.nombre

    def __str__(self):
        return '%s' % self.nombre

    class Meta:
        verbose_name = 'Edicion de herramienta'
        verbose_name_plural = 'Ediciones de herramienta'

    def editor(self):
        if self.usuarioHerramienta:
            if self.usuarioHerramienta.usuario:
                return '%s %s' % (self.usuarioHerramienta.usuario.first_name, self.usuarioHerramienta.usuario.last_name)
        return '----- -----'



    editor.short_description = 'Editor'
