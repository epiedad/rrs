# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0014_auto_20170426_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retreat',
            name='recurring_datetime',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Recurring Date/Time'),
        ),
    ]
