# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-03 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_space', '0015_auto_20160701_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='video_link',
            new_name='youtube_link',
        ),
    ]
