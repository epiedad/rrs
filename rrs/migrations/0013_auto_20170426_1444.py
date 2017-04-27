# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0012_auto_20170426_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='plan_name',
            field=models.CharField(choices=[('sun', 'Sunday Meal'), ('sat', 'Saturday Meal')], db_index=True, max_length=100),
        ),
    ]
