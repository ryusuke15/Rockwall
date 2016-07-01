# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-01 17:42
from __future__ import unicode_literals

import coffee_shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_shop', '0018_mailing_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=coffee_shop.models.blog_image_location),
        ),
    ]