# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0013_auto_20160915_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartoption',
            name='is_select_or_not',
            field=models.BooleanField(default=False),
        ),
    ]
