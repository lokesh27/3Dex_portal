# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0006_auto_20160405_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 5, 10, 9, 47, 359000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
