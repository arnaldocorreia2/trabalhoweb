# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 23:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apostas', '0003_resultado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultado',
            old_name='valor_gol_time_1',
            new_name='valor_gol_time',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='valor_gol_time_2',
        ),
    ]
