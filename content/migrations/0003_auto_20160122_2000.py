# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_lesson_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_description',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
