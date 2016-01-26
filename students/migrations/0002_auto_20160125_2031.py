# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, default=0, max_length=20),
            preserve_default=False,
        ),
    ]
