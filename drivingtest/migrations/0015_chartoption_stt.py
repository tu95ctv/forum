# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0014_chartoption_is_select_or_not'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartoption',
            name='stt',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
