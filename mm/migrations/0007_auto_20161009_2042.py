# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 23:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0006_change_meter_meterhistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meter',
            options={'verbose_name': 'Medidor', 'verbose_name_plural': 'Medidores'},
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='meter',
        ),
        migrations.AddField(
            model_name='history',
            name='channel_1_pulse',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='channel_2_pulse',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='channel_3_pulse',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='mm',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='mm.Mm'),
            preserve_default=False,
        ),
    ]
