# -*- coding: utf-8 -*-
#signal tools
from herramienta import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=models.Herramienta)
def write_update(sender, instance, **kwarg):
    values={'herramienta':instance}
    for key ,value  in instance.changes().items():
        values.update({key:value[0]})
    models.HerramientaEdicion.objects.create(**values)

@receiver(post_save, sender=models.HerramientaEdicion)
def write_update_herramienta(sender, instance, **kwarg):
    values ={}
    herramienta =  models.Herramienta.objects.filter(id=instance.herramienta.id)
    if herramienta:
        for key, value in instance.changes().items():
            values.update({key: value[1]})
        print values
        try:
            del values['creacion']
            del values['usuarioHerramienta_id']
            del values['herramienta_id']
        except KeyError:
            pass
        herramienta.update(**values)






