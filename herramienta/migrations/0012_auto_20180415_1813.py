# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-15 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herramienta', '0011_auto_20180415_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herramienta',
            name='sistema_operativo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='herramientaedicion',
            name='sistema_operativo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
