# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artcenter', '0019_auto_20170102_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performer',
            old_name='pemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='performer',
            old_name='pname',
            new_name='name',
        ),
    ]
