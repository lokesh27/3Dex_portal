# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20160124_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='video_link',
        ),
        migrations.AddField(
            model_name='lesson',
            name='ppt_link',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
    ]
