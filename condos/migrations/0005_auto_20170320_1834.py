# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condos', '0004_auto_20170320_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bedroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
            ],
            options={
                'verbose_name': 'Bedroom',
                'verbose_name_plural': 'Bedroom',
            },
        ),
        migrations.CreateModel(
            name='BedroomQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('BOTH', 'Both'), ('LEASE', 'Lease'), ('RENT', 'Rent')], max_length=10, verbose_name='Type')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('bedroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bedroom_offer', to='condos.Bedroom', verbose_name='Bedroom')),
            ],
            options={
                'verbose_name': 'Bedroom Quantity',
                'verbose_name_plural': 'Bedroom Quantity',
            },
        ),
        migrations.AddField(
            model_name='condo',
            name='county',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='County'),
        ),
        migrations.AddField(
            model_name='condo',
            name='fitness_center',
            field=models.BooleanField(default=False, verbose_name='Fitness Center'),
        ),
        migrations.AddField(
            model_name='condo',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Info'),
        ),
        migrations.AddField(
            model_name='condo',
            name='location',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='condo',
            name='market',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Market'),
        ),
        migrations.AddField(
            model_name='condo',
            name='parking_spaces',
            field=models.IntegerField(blank=True, null=True, verbose_name='Parking Spaces'),
        ),
        migrations.AddField(
            model_name='condo',
            name='pets',
            field=models.BooleanField(default=False, verbose_name='Pets'),
        ),
        migrations.AddField(
            model_name='condo',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='condo',
            name='pool',
            field=models.BooleanField(default=False, verbose_name='Pool'),
        ),
        migrations.AddField(
            model_name='condo',
            name='story_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Stories'),
        ),
        migrations.AddField(
            model_name='condo',
            name='unit_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Units'),
        ),
        migrations.AddField(
            model_name='condo',
            name='valet_parking',
            field=models.BooleanField(default=False, verbose_name='Valet Parking'),
        ),
        migrations.AddField(
            model_name='condo',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Year'),
        ),
        migrations.AddField(
            model_name='bedroomquantity',
            name='condo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Condo_offer', to='condos.Condo', verbose_name='Condo'),
        ),
    ]
