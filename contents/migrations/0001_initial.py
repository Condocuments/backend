# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 18:01
from __future__ import unicode_literals

import condocument_settings.helpers.enum
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('condos', '0004_auto_20170320_1801'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.FileField(upload_to='info', verbose_name='Info')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('type', models.CharField(choices=[('CONDO', 'Condo'), ('USER', 'User')], default=condocument_settings.helpers.enum.ContentType('Condo'), max_length=10, verbose_name='Type')),
                ('condo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='condo_contents', to='condos.Condo', verbose_name='Condo')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_contents', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Contents',
                'verbose_name': 'Content',
            },
        ),
    ]
