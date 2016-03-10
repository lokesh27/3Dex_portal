# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_upload_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
