# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artcenter', '0029_auto_20170114_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Receptionist', 'Receptionist'), ('Technician', 'Technician'), ('Photographer', 'Photographer'), ('Assistence', 'Assistence')], default='Assistence', max_length=200),
        ),
    ]
