# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('date', models.DateTimeField()),
                ('up', models.IntegerField()),
                ('down', models.IntegerField()),
            ],
        ),
    ]
