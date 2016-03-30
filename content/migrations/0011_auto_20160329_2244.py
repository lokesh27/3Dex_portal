# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20160329_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='link',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
