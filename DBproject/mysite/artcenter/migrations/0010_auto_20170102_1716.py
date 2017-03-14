# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 09:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artcenter', '0009_timeofprogram_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeofprogram',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0, 3600)),
        ),
    ]
