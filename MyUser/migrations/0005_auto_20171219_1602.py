# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-19 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyUser', '0004_userprofile_img_r'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='headimg',
            field=models.ImageField(blank=True, default='images/head/default.thumb.jpg', upload_to='images/head'),
        ),
    ]
