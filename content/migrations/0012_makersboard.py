# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20160329_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='MakersBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgfile', models.ImageField(upload_to=b'')),
                ('student_name', models.CharField(max_length=30)),
                ('student_class', models.IntegerField()),
                ('student_school', models.CharField(max_length=30)),
            ],
        ),
    ]
