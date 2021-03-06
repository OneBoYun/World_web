# Generated by Django 2.0.8 on 2018-08-14 16:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stype', models.CharField(max_length=64, verbose_name='活动类型')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='活动名称')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(default=datetime.datetime(2018, 9, 13, 16, 54, 7, 797127), verbose_name='结束时间')),
                ('order_no', models.IntegerField(verbose_name='排序')),
                ('st', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Sale_type', verbose_name='活动类型')),
            ],
        ),
    ]
