# Generated by Django 2.1 on 2018-08-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_auto_20180809_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_option',
            name='integral',
            field=models.IntegerField(blank=True, default=0, help_text='1积分等于RMB一元，客户可用于积分抵扣', null=True, verbose_name='积分'),
        ),
    ]
