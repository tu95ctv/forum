# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0015_chartoption_stt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartoption',
            name='stt',
            field=models.IntegerField(null=True),
        ),
    ]
