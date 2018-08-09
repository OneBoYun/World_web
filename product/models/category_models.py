from django.db import models
from .filter_models import Filter


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="category/",
                              null=True,
                              blank=True,
                              verbose_name="图片")

    parend = models.ForeignKey("self",
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               verbose_name="父类")

    top = models.BooleanField(verbose_name="置顶",
                              help_text="只适用顶层分类",
                              default=False)
    column = models.IntegerField(verbose_name="子分类",
                                 help_text="拥有多少层子分类",
                                 default=1)

    sort_order = models.IntegerField(verbose_name="排序",
                                     default=0)

    status = models.BooleanField(verbose_name="ON/OFF",
                                 help_text="开启或者关闭分类",
                                 default=True)

    date_added = models.DateTimeField(verbose_name="添加日期",
                                      auto_now_add=True)

    date_mofified = models.DateTimeField(verbose_name="修改日期",
                                         auto_now=True)


class Category_description(models.Model):
    category_description_id = models.AutoField(primary_key=True)
    category = models.OneToOneField(Category,
                                    on_delete=models.CASCADE,
                                    verbose_name="分类")
    name = models.CharField(verbose_name="类名",
                            max_length=255)

    description = models.TextField(verbose_name="详情",
                                   null=True,
                                   blank=True)

    meta_title = models.CharField(verbose_name="META TITLE",
                                  null=True,
                                  blank=True,
                                  max_length=255)

    meta_description = models.CharField(verbose_name="META TITLE",
                                  null=True,
                                  blank=True,
                                  max_length=255)

    meta_keyword = models.CharField(verbose_name="META KEYWORD",
                                    null=True,
                                    blank=True,
                                    max_length=255)


class Category_filter(models.Model):
    category_filter_id = models.AutoField(primary_key=True)
    filter = models.ForeignKey(Filter,
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name="过滤标签")
    category = models.OneToOneField(Category,
                                    on_delete=models.CASCADE,
                                    verbose_name="分类")