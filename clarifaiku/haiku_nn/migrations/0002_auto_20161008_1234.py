# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haiku_nn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='theme',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]