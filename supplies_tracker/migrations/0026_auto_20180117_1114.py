# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-17 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies_tracker', '0025_auto_20180117_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
