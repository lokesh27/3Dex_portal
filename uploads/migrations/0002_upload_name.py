# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
