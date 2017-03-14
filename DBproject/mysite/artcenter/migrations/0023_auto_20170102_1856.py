# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artcenter', '0022_auto_20170102_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audience_name', models.CharField(max_length=40)),
                ('audience_email', models.EmailField(max_length=100)),
                ('comment', models.CharField(max_length=800)),
                ('rating', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], default='3', max_length=200)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artcenter.Program')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together=set([('program', 'ticket_type')]),
        ),
    ]