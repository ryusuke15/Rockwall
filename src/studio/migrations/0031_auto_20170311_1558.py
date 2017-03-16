# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 20:58
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0030_blog_cropping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
