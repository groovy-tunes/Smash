# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Annotation', '0013_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poster',
            name='votedOn',
        ),
        migrations.AddField(
            model_name='poster',
            name='votedOn',
            field=models.ManyToManyField(to='Annotation.Post'),
        ),
    ]
