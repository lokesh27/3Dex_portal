# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20160305_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(blank=True, default=0, upload_to='profile_pictures'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.IntegerField(choices=[(6, 6), (7, 7), (8, 8), (9, 9)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='school_name',
            field=models.CharField(choices=[('abc', 'abc'), ('xyz', 'xyz'), ('qwe', 'qwe')], max_length=30),
        ),
    ]
