# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0008_myselectchartoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='myselectchartoption',
            name='Name',
            field=models.CharField(default=1, unique=True, max_length=400),
            preserve_default=False,
        ),
    ]
