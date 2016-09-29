# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0010_chartoption_options_data_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='LuuOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(unique=True, max_length=400)),
                ('options_data_list', models.CharField(max_length=400, null=True, blank=True)),
            ],
        ),
    ]
