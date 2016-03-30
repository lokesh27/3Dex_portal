# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_remove_lesson_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='for_class',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(6, 6), (7, 7), (8, 8), (9, 9)], default=0, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='for_school',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('abc', 'abc'), ('xyz', 'xyz'), ('qwe', 'qwe')], default=0, max_length=11),
            preserve_default=False,
        ),
    ]
