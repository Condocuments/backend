# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='condo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='condos.Condo', verbose_name='Condo'),
        ),
    ]