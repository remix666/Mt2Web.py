# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-23 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0002_auto_20180221_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='registroConectados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Conectados por fecha',
                'verbose_name_plural': 'Conectados por fecha',
            },
        ),
        migrations.DeleteModel(
            name='Conectados_Fecha',
        ),
    ]
