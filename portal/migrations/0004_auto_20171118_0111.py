# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20171118_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='especie',
            name='slug',
            field=models.SlugField(default='slug', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raca',
            name='slug',
            field=models.SlugField(default='slug', unique=True),
            preserve_default=False,
        ),
    ]
