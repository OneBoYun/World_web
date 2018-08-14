# Generated by Django 2.0.8 on 2018-08-14 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_auto_20180814_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 15, 17, 57, 19, 101204), verbose_name='有效日期'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='serial_number',
            field=models.CharField(default='20180814175719391012735', max_length=32, verbose_name='流水号'),
        ),
        migrations.AlterField(
            model_name='change',
            name='return_id',
            field=models.CharField(default='20180814175719391017401', max_length=32, verbose_name='退款编号'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_no',
            field=models.CharField(default='20180814175719639102859', max_length=32, verbose_name='券编号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_no',
            field=models.CharField(default='20180814175719391037214', max_length=32, verbose_name='流水号'),
        ),
    ]