# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0018_auto_20170426_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='dependent',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
