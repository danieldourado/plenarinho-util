# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-06 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0009_auto_20180306_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pergunta',
            old_name='texto',
            new_name='texto2',
        ),
    ]
