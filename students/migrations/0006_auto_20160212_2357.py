# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20160202_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.CharField(max_length=11),
        ),
    ]
