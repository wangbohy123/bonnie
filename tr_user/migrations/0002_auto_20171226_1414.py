# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-26 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tr_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translater',
            name='credit_level',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='translater',
            name='score_sum',
            field=models.IntegerField(default=0, null=True),
        ),
    ]