# Generated by Django 2.0.8 on 2018-08-13 16:26

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20180810_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_description',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='商品详情'),
        ),
    ]