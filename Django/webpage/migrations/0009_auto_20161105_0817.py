# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0008_auto_20161105_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nick_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(upload_to=b''),
        ),
    ]