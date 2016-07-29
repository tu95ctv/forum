# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ul_order', models.IntegerField(default=1)),
                ('rg_order', models.IntegerField(default=2)),
                ('up_order', models.IntegerField(default=3)),
                ('show_not_my_link', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ForumTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sleep_time', models.IntegerField(default=60)),
                ('url', models.CharField(max_length=100, null=True, blank=True)),
                ('uname', models.CharField(max_length=100, null=True, blank=True)),
                ('passwd', models.CharField(max_length=100, null=True, blank=True)),
                ('newthread_url', models.CharField(max_length=100, null=True, blank=True)),
                ('music', models.CharField(max_length=100, null=True, blank=True)),
                ('tv_show', models.CharField(max_length=100, null=True, blank=True)),
                ('movie', models.CharField(max_length=100, null=True, blank=True)),
                ('HDmovie', models.CharField(max_length=100, null=True, blank=True)),
                ('software', models.CharField(max_length=100, null=True, blank=True)),
                ('game', models.CharField(max_length=100, null=True, blank=True)),
                ('anime', models.CharField(max_length=100, null=True, blank=True)),
                ('mobile', models.CharField(max_length=100, null=True, blank=True)),
                ('ebook', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeechSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=100, null=True, blank=True)),
                ('music', models.CharField(max_length=100, null=True, blank=True)),
                ('tv_show', models.CharField(max_length=100, null=True, blank=True)),
                ('movie', models.CharField(max_length=100, null=True, blank=True)),
                ('HDmovie', models.CharField(max_length=100, null=True, blank=True)),
                ('software', models.CharField(max_length=100, null=True, blank=True)),
                ('game', models.CharField(max_length=100, null=True, blank=True)),
                ('anime', models.CharField(max_length=100, null=True, blank=True)),
                ('mobile', models.CharField(max_length=100, null=True, blank=True)),
                ('ebook', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posted_link', models.CharField(max_length=100, null=True, blank=True)),
                ('posted_datetime', models.DateTimeField(auto_now_add=True)),
                ('forum', models.ForeignKey(related_name='postLog', to='drivingtest.ForumTable')),
            ],
        ),
        migrations.CreateModel(
            name='TaiXiu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phien_so', models.IntegerField(unique=True)),
                ('cau_1', models.IntegerField()),
                ('cau_2', models.IntegerField()),
                ('cau_3', models.IntegerField()),
                ('tong', models.IntegerField()),
                ('tai_1_xiu_0', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ulnew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200, verbose_name=b'model verbose name')),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=50000, null=True, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rg', models.CharField(max_length=2000, null=True, blank=True)),
                ('ul', models.CharField(max_length=2000, null=True, blank=True)),
                ('up', models.CharField(max_length=2000, null=True, blank=True)),
                ('myrg', models.CharField(max_length=2000, null=True, blank=True)),
                ('myul', models.CharField(max_length=2000, null=True, blank=True)),
                ('myup', models.CharField(max_length=2000, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='postlog',
            name='posted_topic',
            field=models.ForeignKey(related_name='postLog', to='drivingtest.Ulnew'),
        ),
        migrations.AddField(
            model_name='forumtable',
            name='postedLog_dat_tenJ_cungduoc_link',
            field=models.ManyToManyField(related_name='forumback', through='drivingtest.PostLog', to='drivingtest.Ulnew'),
        ),
    ]
