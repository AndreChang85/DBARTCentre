# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artcenter', '0027_auto_20170102_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='audience_number',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
