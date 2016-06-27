# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_shop', '0010_blog_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='created',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='blog',
            name='publish',
            field=models.DateField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]