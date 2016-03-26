# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160326_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
