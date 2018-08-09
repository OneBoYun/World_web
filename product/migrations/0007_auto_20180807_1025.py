# Generated by Django 2.1 on 2018-08-07 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_description_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_discount',
        ),
        migrations.AddField(
            model_name='product_discount',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='商品折扣'),
            preserve_default=False,
        ),
    ]
