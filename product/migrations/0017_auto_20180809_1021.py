# Generated by Django 2.1 on 2018-08-09 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_remove_product_promotion_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_description',
            name='language_id',
            field=models.ForeignKey(blank=True, help_text='提供不同语言针对不同国家', null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Language', verbose_name='语言'),
        ),
        migrations.AlterField(
            model_name='product_special',
            name='price',
            field=models.DecimalField(decimal_places=9, help_text='原价的减去折扣百分比', max_digits=19, verbose_name='折扣百分比%'),
        ),
    ]