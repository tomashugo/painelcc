# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crews', '0008_auto_20160929_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='registration',
            field=models.CharField(default=b'u0000', max_length=6),
        ),
    ]
