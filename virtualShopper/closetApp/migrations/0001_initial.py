# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothingType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('price', models.IntegerField(default=0)),
                ('picture', models.ImageField(upload_to=b'')),
                ('purchased_at', models.DateTimeField(auto_now=True)),
                ('pos_x', models.IntegerField(verbose_name=0)),
                ('pos_y', models.IntegerField(verbose_name=-5)),
                ('pos_z', models.IntegerField(verbose_name=-5)),
                ('size', models.CharField(unique=True, max_length=128)),
                ('color', models.CharField(unique=True, max_length=128)),
                ('season', models.CharField(unique=True, max_length=128)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
