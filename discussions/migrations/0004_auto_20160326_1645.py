# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0003_auto_20160324_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='for_class',
            field=models.IntegerField(choices=[(6, 6), (7, 7), (8, 8), (9, 9)], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='for_school',
            field=models.CharField(choices=[('abc', 'abc'), ('xyz', 'xyz'), ('qwe', 'qwe')], default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
