# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crews', '0010_auto_20160930_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_km', models.DateTimeField(verbose_name=b'data do km')),
                ('km', models.CharField(max_length=6)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crews.Car')),
            ],
        ),
    ]