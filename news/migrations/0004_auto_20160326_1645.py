# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='for_school',
            field=models.CharField(choices=[('abc', 'abc'), ('xyz', 'xyz'), ('qwe', 'qwe')], max_length=30),
        ),
    ]
