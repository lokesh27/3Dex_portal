# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20160213_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_description',
        ),
        migrations.AddField(
            model_name='lesson',
            name='full_description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='short_description',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
