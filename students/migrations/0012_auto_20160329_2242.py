# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20160326_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school_name',
            field=models.CharField(choices=[('abc', 'abc'), ('xyz', 'xyz'), ('qwe', 'qwe'), ('Happy School', 'Happy School')], max_length=30),
        ),
    ]
