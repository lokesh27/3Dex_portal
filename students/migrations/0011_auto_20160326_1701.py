# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20160326_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
