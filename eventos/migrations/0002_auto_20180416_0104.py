# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 04:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='qualidadetecnica',
            new_name='qualitecnica',
        ),
    ]
