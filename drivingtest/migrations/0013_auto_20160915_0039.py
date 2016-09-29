# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0012_auto_20160915_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luuoption',
            name='Name',
            field=models.CharField(unique=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='luuoption',
            name='options_data_list',
            field=models.CharField(max_length=40000, null=True, blank=True),
        ),
    ]
