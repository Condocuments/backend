# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condos', '0007_auto_20170321_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='type',
            field=models.CharField(choices=[('BOTH', 'Both'), ('LEASE', 'Lease'), ('RENT', 'Rent')], default='Both', max_length=10, verbose_name='Type'),
        ),
    ]
