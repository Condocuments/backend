# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 20:50
from __future__ import unicode_literals

from django.db import migrations, models
import people.models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='license',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='ID or License'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ssn',
            field=models.CharField(blank=True, max_length=15, unique=True, validators=[people.models.validate_ssn], verbose_name='SSN'),
        ),
    ]
