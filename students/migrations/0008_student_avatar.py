# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_student_class_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default=0, upload_to='profile_pictures'),
            preserve_default=False,
        ),
    ]
