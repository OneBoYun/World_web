from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Sale_type(models.Model):
    title = models.CharField(verbose_name="标题",
                             max_length=64)
    sub_title = models.CharField(verbose_name="副级标题",
                                 max_length=64)

    def __str__(self):
        return self.title

class Sales(models.Model):
    st = models.ForeignKey(Sale_type,
                           on_delete=models.CASCADE,
                           verbose_name="促销模块")

    stype = models.CharField(verbose_name="活动类型",
                             max_length=64)

    style = models.IntegerField(verbose_name="样式",
                                choices=((1, "one"),
                                         (2, "two"),
                                         (3, "three"),
                                         (4, "last")),
                                default=1)

    link = models.CharField(verbose_name="超链接",
                            max_length=254,
                            default="")

    name = models.CharField(verbose_name="活动名称",
                            max_length=64)

    image = models.ImageField(verbose_name="活动图片",
                              upload_to="sales/")

    start_time = models.DateTimeField(verbose_name="开始时间",
                                      default=timezone.now)

    end_time = models.DateTimeField(verbose_name="结束时间",
                                    default=timezone.now() + datetime.timedelta(days=30))

    order_no = models.IntegerField(verbose_name="排序",
                                   default=0)

    def __str__(self):
        return self.name