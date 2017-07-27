# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 02:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_auto_20170718_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='Authors.Author'),
        ),
    ]
