# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0006_auto_20160902_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(unique=True, max_length=400)),
            ],
        ),
    ]
