# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20160126_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]
