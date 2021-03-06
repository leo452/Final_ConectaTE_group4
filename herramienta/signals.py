# -*- coding: utf-8 -*-
from herramienta import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
#senales para guardar la herramienta y las ediciones de la misma y tenerla en estado de borrador
@receiver(post_save, sender=models.Herramienta)
def write_update(sender, instance, **kwarg):
    if kwarg["created"]:
        values = {
            'herramienta': instance,
            'nombre':instance.nombre,
            'descripcion':instance.descripcion,
            'licencia':instance.licencia,
            'usos':instance.usos,
            'enlaces':instance.enlaces,
            'descarga_url':instance.descarga_url,
            'sistema_operativo':instance.sistema_operativo,
            'version':instance.version,
            'integracion_lms':instance.integracion_lms,
            'informacion':instance.informacion,
            'documentacion':instance.documentacion,
            'tipo':instance.tipo

        }

    else:
        values={'herramienta':instance}
        for key ,value  in instance.changes().items():
            if not key == 'owner_id' and key != 'id' and key!='estado':
                values.update({key:value[0]})
    models.HerramientaEdicion.objects.create(**values)

@receiver(post_save, sender=models.HerramientaEdicion)
def write_update_herramienta(sender, instance, **kwarg):
    values ={}
    herramienta =  models.Herramienta.objects.filter(id=instance.herramienta.id)
    if herramienta:
        for key, value in instance.changes().items():

            if key != 'observacion' and key != 'creacion' and key != 'usuarioHerramienta_id' and key != 'herramienta_id' and key != 'revision_id' and key != 'id':
                values.update({key: value[1]})

        herramienta.update(**values)





