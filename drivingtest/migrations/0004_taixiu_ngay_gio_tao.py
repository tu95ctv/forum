# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0003_auto_20160727_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='taixiu',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 14, 59, 10, 78000, tzinfo=utc), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
            preserve_default=False,
        ),
    ]
