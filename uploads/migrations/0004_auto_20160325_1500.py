# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_upload_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='stlfile',
        ),
        migrations.AddField(
            model_name='upload',
            name='file',
            field=models.FileField(default=0, upload_to='submissions/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
