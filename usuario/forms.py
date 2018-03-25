# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.admin import widgets
import models


class UsuarioForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['email'].label = "Correo Electrónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['groups'].label = "Perfil"
    # end def

    class Meta:
        model = models.Usuario
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2','groups']
    # end class
# end class


class UsuarioEditFormAdmin(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(UsuarioEditFormAdmin, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Correo Electrónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['groups'].label = "Perfil"

    # end def

    class Meta:
        model = models.Usuario
        fieldsets = ['username', 'first_name',
                     'last_name', 'email','groups']
        exclude = [ 'password1', 'password2']
    # end class
# end class