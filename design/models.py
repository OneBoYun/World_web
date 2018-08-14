from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Banner_mode(models.Model):
    """banner类型"""
    name = models.CharField(verbose_name="名称",
                            max_length=64)
    effect = models.CharField(verbose_name="效果",
                              max_length=64,
                              null=True,
                              blank=True)

    delay_time = models.IntegerField(verbose_name="延时",
                                     help_text="以秒为单位")

    auto_slide = models.BooleanField(verbose_name="自动播放",
                                     default=True)

    hover = models.BooleanField(verbose_name="循环",
                                default=True)

    status = models.BooleanField(verbose_name="状态",
                                 help_text="开启/关闭",
                                 default=True)

    def __str__(self):
        return self.name


class Banner(models.Model):
    """banner"""
    mode = models.ForeignKey(Banner_mode,
                             on_delete=models.CASCADE,
                             verbose_name="类型名字")

    title = models.CharField(verbose_name="标题",
                             max_length=64)

    sub_title = models.CharField(verbose_name="二级标题",
                                 max_length=64)

    description = RichTextUploadingField(verbose_name="详情")

    link = models.CharField(verbose_name="链接",
                            max_length=254)

    image = models.ImageField(verbose_name="图片",
                              upload_to="design/banner/")

    def __str__(self):
        return self.title