# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-04 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0024_auto_20170105_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='meter',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mm.Company'),
        ),
        migrations.AddField(
            model_name='mm',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mm.Company'),
        ),
    ]