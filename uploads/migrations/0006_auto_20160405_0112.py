# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0005_upload_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='class_name',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='school_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
