# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-08 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0015_remove_relatoriommversusconsumo_expira'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatoriocorrentezerada',
            name='data_expira',
            field=models.DateTimeField(blank=True, null=True, verbose_name='data_expira'),
        ),
    ]
