# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closetApp', '0002_auto_20170211_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingtype',
            name='pos_x',
            field=models.IntegerField(verbose_name=14),
        ),
        migrations.AlterField(
            model_name='clothingtype',
            name='pos_y',
            field=models.IntegerField(verbose_name=-4),
        ),
    ]
