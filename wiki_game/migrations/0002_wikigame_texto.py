# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-21 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki_game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikigame',
            name='texto',
            field=models.TextField(default='', null=True),
        ),
    ]