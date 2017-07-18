# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 02:19
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=18, unique=True)),
                ('date_published', models.DateField()),
                ('cover_photo', models.URLField()),
                ('summary', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('lit_genre', models.CharField(choices=[('sf', 'science fiction'), ('dr', 'drama'), ('ft', 'fantasy'), ('bg', 'biography'), ('ht', 'history'), ('ot', 'others')], max_length=80)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=5)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Book')),
            ],
        ),
    ]