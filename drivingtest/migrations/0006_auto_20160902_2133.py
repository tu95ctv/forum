# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0005_auto_20160902_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datcua',
            old_name='TenTable',
            new_name='tenTable',
        ),
    ]
