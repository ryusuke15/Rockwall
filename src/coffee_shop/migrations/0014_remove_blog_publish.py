# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_shop', '0013_auto_20160617_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='publish',
        ),
    ]