# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-07 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0025_relatoriofraudenaoincrementada_justificado'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatorioalteracoesmedidor',
            name='alvo_gerado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='relatoriocorrentezerada',
            name='alvo_gerado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='relatoriofraudenaoincrementada',
            name='alvo_gerado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='relatoriommversusconsumo',
            name='alvo_gerado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='relatorioquedadeconsumo',
            name='alvo_gerado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='relatoriotensaozerada',
            name='alvo_gerado',
            field=models.BooleanField(default=False),
        ),
    ]
