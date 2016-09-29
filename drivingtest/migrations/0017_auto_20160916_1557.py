# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0016_auto_20160916_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartoption',
            name='stt',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
