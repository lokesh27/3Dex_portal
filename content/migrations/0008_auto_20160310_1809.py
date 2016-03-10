# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_lesson_allow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='ppt_link',
        ),
        migrations.AddField(
            model_name='lesson',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='lesson',
            name='type',
            field=models.CharField(choices=[('VID', 'Video'), ('PPT', 'Presentation'), ('PDF', 'Pdf')], default=0, max_length=20),
            preserve_default=False,
        ),
    ]
