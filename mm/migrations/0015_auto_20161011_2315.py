# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0014_auto_20161011_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterhistory',
            name='meter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meterhistory', to='mm.Meter'),
        ),
    ]