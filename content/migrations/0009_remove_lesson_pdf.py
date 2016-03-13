# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20160310_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='pdf',
        ),
    ]
