# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 18:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0012_remove_blog_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Spotlight',
            new_name='spotlight',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='Upcoming',
            new_name='upcoming',
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 6, 18, 18, 30, 32, 137135, tzinfo=utc)),
            preserve_default=False,
        ),
    ]