# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-08 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_picture_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
