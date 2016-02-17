# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20160212_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_name',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
