# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_auto_20161018_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='register',
            options={'verbose_name': 'Registrador', 'verbose_name_plural': 'Registradores'},
        ),
        migrations.AlterField(
            model_name='billing',
            name='reader_msg',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
