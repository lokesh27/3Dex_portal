# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20160217_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='allow',
            field=models.BooleanField(default=False),
        ),
    ]
