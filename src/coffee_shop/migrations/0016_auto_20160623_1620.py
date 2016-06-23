# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 20:20
from __future__ import unicode_literals

import coffee_shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_shop', '0015_remove_blog_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='draft',
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=coffee_shop.models.blog_image_location, width_field='width_field'),
        ),
    ]
