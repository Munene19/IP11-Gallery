# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-04 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
