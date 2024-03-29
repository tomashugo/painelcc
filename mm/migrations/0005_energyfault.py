# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0004_auto_20160930_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyFault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_hour', models.DateTimeField(verbose_name='inicio da falta')),
                ('end_hour', models.DateTimeField(verbose_name='fim da falta')),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mm.Consumer')),
            ],
        ),
    ]
