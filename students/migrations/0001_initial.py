# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20, null=True)),
                ('email_id', models.CharField(max_length=40)),
                ('phone_no', models.CharField(max_length=10)),
                ('school_name', models.CharField(max_length=50)),
            ],
        ),
    ]
