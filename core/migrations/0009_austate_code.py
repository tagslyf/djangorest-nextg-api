# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20160920_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='austate',
            name='code',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]
