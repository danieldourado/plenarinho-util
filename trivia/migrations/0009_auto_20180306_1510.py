# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-06 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0008_remove_pergunta_texto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pergunta',
            old_name='texto2',
            new_name='texto',
        ),
    ]
