# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 21:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_shop', '0006_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(default=datetime.datetime(2016, 6, 16, 21, 38, 5, 481569, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
