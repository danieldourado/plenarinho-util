# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2021-07-16 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0008_auto_20210716_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='endereco',
        ),
    ]
