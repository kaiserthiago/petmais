# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20171123_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='petquestion',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2017-11-11 16:46:00'),
            preserve_default=False,
        ),
    ]
