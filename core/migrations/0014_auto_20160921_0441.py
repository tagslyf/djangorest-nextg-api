# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 04:41
from __future__ import unicode_literals

import core.methods
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20160921_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=core.methods.school_logo_upload_path_handler),
        ),
    ]