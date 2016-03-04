# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_student_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
    ]
