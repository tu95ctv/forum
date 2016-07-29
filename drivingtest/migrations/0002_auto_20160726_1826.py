# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taixiu',
            name='cau_1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='taixiu',
            name='cau_2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='taixiu',
            name='cau_3',
            field=models.IntegerField(null=True),
        ),
    ]
