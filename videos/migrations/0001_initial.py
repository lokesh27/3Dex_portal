# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_description', models.CharField(max_length=50)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('video_link', models.TextField()),
            ],
        ),
    ]
