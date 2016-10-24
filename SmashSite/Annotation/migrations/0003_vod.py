# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Annotation', '0002_post_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('url', models.URLField(default='')),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
