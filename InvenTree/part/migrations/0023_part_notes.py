# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0022_auto_20180417_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
