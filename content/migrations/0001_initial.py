# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=20)),
                ('lesson_description', models.CharField(max_length=50)),
                ('added_date', models.DateTimeField(verbose_name='date added')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='lesson',
            field=models.ForeignKey(to='content.Lesson'),
        ),
    ]
