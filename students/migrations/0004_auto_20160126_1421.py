# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_secret_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='secret_key',
            new_name='password',
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
