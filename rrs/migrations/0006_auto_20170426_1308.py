# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0005_auto_20170426_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendee',
            name='official_name',
        ),
        migrations.AddField(
            model_name='attendee',
            name='first_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendee',
            name='last_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dependent',
            name='first_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dependent',
            name='last_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
