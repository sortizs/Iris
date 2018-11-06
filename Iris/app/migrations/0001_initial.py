# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('lastname', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=254)),
                ('age', models.IntegerField(max_length=2)),
            ],
        ),
    ]
