# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_makersboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='makersboard',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
