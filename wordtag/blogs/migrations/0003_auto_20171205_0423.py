# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20171205_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]