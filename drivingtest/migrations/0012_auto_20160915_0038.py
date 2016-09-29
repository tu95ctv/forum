# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0011_luuoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luuoption',
            name='Name',
            field=models.CharField(unique=True, max_length=40000),
        ),
    ]
