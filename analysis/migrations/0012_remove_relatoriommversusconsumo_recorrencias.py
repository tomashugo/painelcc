# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-29 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0011_relatoriommversusconsumo_recorrencias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatoriommversusconsumo',
            name='recorrencias',
        ),
    ]