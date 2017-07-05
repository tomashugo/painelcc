# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0022_mm_path'),
        ('analysis', '0016_relatoriocorrentezerada_data_expira'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatorioQuedaDeConsumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.DateField(verbose_name='referencia')),
                ('media_consumo', models.FloatField()),
                ('consumo_referencia', models.FloatField()),
                ('user', models.CharField(blank=True, max_length=20, null=True)),
                ('justificativa', models.TextField(blank=True, null=True)),
                ('data_expira', models.DateField(blank=True, null=True, verbose_name='data_expira')),
                ('data_hora', models.DateTimeField(blank=True, null=True, verbose_name='date_hour_justified')),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mm.Consumer')),
            ],
        ),
    ]
