# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0009_myselectchartoption_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartoption',
            name='options_data_list',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
    ]
