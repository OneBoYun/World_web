# Generated by Django 2.1 on 2018-08-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20180807_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_image',
            name='order',
            field=models.IntegerField(default=0, verbose_name='排序'),
        ),
    ]
