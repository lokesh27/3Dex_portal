# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20160125_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='secret_key',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
