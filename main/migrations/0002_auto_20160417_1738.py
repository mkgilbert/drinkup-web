# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemorderlink',
            name='status',
            field=models.CharField(default='incomplete', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
    ]
