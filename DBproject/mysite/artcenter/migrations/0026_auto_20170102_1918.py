# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artcenter', '0025_do'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Receptionist', 'Receptionist'), ('technician', 'Technician'), ('Photographer', 'Photographer'), ('Assistence', 'Assistence')], default='Assistence', max_length=200),
        ),
        migrations.AlterField(
            model_name='manager',
            name='program_type',
            field=models.CharField(choices=[('Music', 'Music'), ('Speech', 'Speech'), ('Photo', 'Photo')], default='Music', max_length=200),
        ),
        migrations.AlterField(
            model_name='program',
            name='program_type',
            field=models.CharField(choices=[('Music', 'Music'), ('Speech', 'Speech'), ('Photo', 'Photo')], default='Music', max_length=200),
        ),
        migrations.AlterField(
            model_name='works_on',
            name='job_type',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Receptionist', 'Receptionist'), ('technician', 'Technician'), ('Photographer', 'Photographer'), ('Assistence', 'Assistence')], default='Assistence', max_length=200),
        ),
    ]
