# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20171120_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='cometario',
            new_name='comentario',
        ),
    ]
