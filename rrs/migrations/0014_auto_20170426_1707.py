# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0013_auto_20170426_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retreat',
            name='recurring_datetime',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Retreat Date/Time'),
        ),
        migrations.AlterField(
            model_name='retreat',
            name='retreat_datetime',
            field=models.DateTimeField(db_index=True, verbose_name='Retreat Date/Time'),
        ),
    ]
