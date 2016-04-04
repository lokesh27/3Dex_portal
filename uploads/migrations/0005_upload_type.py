# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0004_auto_20160325_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='type',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
