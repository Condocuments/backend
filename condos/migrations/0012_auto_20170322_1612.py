# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condos', '0011_auto_20170322_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='condo',
            name='slug',
            field=models.SlugField(default='', max_length=150, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bedroomquantity',
            name='condo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='condo_offer', to='condos.Condo', verbose_name='Condo'),
        ),
    ]
