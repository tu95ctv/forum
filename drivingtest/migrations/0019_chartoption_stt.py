# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0018_remove_chartoption_stt'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartoption',
            name='stt',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
