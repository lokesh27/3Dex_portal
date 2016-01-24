# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20160122_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
