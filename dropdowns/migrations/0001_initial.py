# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upload_dropdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=30)),
                ('for_school', multiselectfield.db.fields.MultiSelectField(choices=[('abc', 'abc'), ('xyz', 'xyz'), ('qwe', 'qwe')], max_length=11)),
                ('for_class', multiselectfield.db.fields.MultiSelectField(choices=[(6, 6), (7, 7), (8, 8), (9, 9)], max_length=7)),
                ('show', models.BooleanField(default=False)),
            ],
        ),
    ]
