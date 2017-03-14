# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ptype', models.CharField(choices=[('MC', 'Music'), ('SP', 'Speech'), ('PT', 'Photo')], default='MC', max_length=200)),
                ('cost', models.IntegerField(default=0)),
                ('audience_number', models.IntegerField(default=0)),
            ],
        ),
    ]
