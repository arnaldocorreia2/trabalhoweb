# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apostas', '0002_auto_20160417_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_gol_time_1', models.IntegerField()),
                ('valor_gol_time_2', models.IntegerField()),
                ('partida', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apostas.Partida')),
                ('time', models.ManyToManyField(to='apostas.Time')),
            ],
        ),
    ]