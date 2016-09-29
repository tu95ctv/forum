# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drivingtest', '0004_taixiu_ngay_gio_tao'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatCua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cua_tai_hay_xiu', models.IntegerField()),
                ('phien_cua', models.IntegerField(unique=True)),
                ('so_tien', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TenTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='taixiu',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AddField(
            model_name='datcua',
            name='TenTable',
            field=models.ForeignKey(to='drivingtest.TenTable', blank=True),
        ),
    ]
