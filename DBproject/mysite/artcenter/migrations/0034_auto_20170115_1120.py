# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artcenter', '0033_remove_equipment_equipment_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works_on',
            name='job_type',
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
