# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0002_auto_20160726_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taixiu',
            name='cau_1',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taixiu',
            name='cau_2',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taixiu',
            name='cau_3',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taixiu',
            name='tong',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
