# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0017_auto_20160916_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chartoption',
            name='stt',
        ),
    ]
