# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artcenter', '0024_auto_20170102_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Do',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artcenter.Employee')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artcenter.Job')),
            ],
        ),
    ]