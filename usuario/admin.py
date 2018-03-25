from django.contrib import admin
import models
import forms
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name']
    search_fields = ['username','first_name', 'last_name']
    form = forms.UsuarioForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.UsuarioEditFormAdmin
        # end if
        return super(UsuarioAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def

admin.site.register(models.Usuario, UsuarioAdmin)