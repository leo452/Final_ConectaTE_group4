# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 05:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herramienta', '0009_auto_20180413_0417'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HerramientasPorAprobar',
            new_name='HerramientaPorAprobar',
        ),
    ]