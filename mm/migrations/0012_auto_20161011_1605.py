# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0011_energyfault_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='mm',
            name='meter_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mm.Meter'),
        ),
        migrations.AddField(
            model_name='mm',
            name='status_batery',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]