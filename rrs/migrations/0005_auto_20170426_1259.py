# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0004_dependent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dependent',
            name='name',
        ),
        migrations.AddField(
            model_name='dependent',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Femail')], db_index=True, max_length=2),
        ),
    ]