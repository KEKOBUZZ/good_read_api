# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 00:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='age',
        ),
    ]