from __future__ import unicode_literals


from django.contrib.auth.models import User
from django.db import models


# modelo de usuario generico que sera utilizado en la aplicacion.
class Usuario(User):
    perfil= models.IntegerField(default=0)
    proyectos =  models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.username
    #
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.is_staff=True
    #     super(User,self).save(*args,**kwargs)