# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='Profile', verbose_name='Profile Picture'),
        ),
    ]
