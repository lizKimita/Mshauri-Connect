# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-19 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0004_auto_20190617_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='forums',
            name='post_cover',
            field=models.ImageField(blank=True, upload_to='cover_pics'),
        ),
    ]
