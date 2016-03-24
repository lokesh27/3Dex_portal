# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0002_auto_20160324_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
