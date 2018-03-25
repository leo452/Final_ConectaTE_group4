# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herramienta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='herramienta',
            name='integracion_lms',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='sistema_operativo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='version',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='herramientaedicion',
            name='integracion_lms',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='herramientaedicion',
            name='sistema_operativo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='herramientaedicion',
            name='version',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
