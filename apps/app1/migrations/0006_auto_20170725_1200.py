# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='full_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
