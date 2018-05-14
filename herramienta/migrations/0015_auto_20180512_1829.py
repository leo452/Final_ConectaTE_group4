# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-12 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('herramienta', '0014_ejemplo_tutorial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='herramienta',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='herramienta',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='herramienta.Herramienta'),
            preserve_default=False,
        ),
    ]
