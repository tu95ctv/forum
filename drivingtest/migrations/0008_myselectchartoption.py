# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0007_chartoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySelectChartOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('myselect', models.ManyToManyField(to='drivingtest.ChartOption')),
            ],
        ),
    ]
