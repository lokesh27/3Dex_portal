# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_makersboard_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makersboard',
            name='student_class',
            field=models.CharField(max_length=10),
        ),
    ]
