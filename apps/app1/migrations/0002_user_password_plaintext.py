# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password_plaintext',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
