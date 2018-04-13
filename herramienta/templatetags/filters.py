from django import template
from django.contrib.auth.models import Group
from herramienta.models import HerramientaPorAprobar

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter(name='has_borrador_access')
def has_borrador_access(user, herramienta):
    return True if is_herramienta_owner(user, herramienta) and herramienta.estado == 0 else False


@register.filter(name='has_revision_access')
def has_revision_access(user, herramienta):
    return True if herramienta.estado == 1 and (has_group(user, "MiembroGTI") or has_group(user, "MiembroConectate")) \
        else False


@register.filter (name='is_herramienta_owner')
def is_herramienta_owner(user, herramienta):
    return True if herramienta.owner.username == user.username else False


@register.filter(name='is_herramienta_posted_by_user')
def is_herramienta_posted_by_user(user, herramienta):
    list_revisiones = HerramientaPorAprobar.objects.filter(herramienta_id=herramienta.id)

    for revision in list_revisiones:
        if revision.owner.username == user.username:
            return True

    return False
