# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 15:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herramienta', '0002_auto_20180325_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='herramienta',
            name='integracion_lms',
        ),
        migrations.RemoveField(
            model_name='herramienta',
            name='sistema_operativo',
        ),
        migrations.RemoveField(
            model_name='herramienta',
            name='version',
        ),
        migrations.RemoveField(
            model_name='herramientaedicion',
            name='integracion_lms',
        ),
        migrations.RemoveField(
            model_name='herramientaedicion',
            name='sistema_operativo',
        ),
        migrations.RemoveField(
            model_name='herramientaedicion',
            name='version',
        ),
    ]
