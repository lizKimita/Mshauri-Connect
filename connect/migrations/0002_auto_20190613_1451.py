# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-13 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forums',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='forums',
            name='post_id',
            field=models.IntegerField(default=0),
        ),
    ]
