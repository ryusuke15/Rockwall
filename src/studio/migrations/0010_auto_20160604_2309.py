# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0009_auto_20160604_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]