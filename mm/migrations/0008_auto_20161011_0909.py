# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0007_auto_20161009_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='change',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='data da alteracao'),
        ),
        migrations.AddField(
            model_name='change',
            name='leitor',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
