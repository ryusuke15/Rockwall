# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_space', '0009_auto_20160623_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
