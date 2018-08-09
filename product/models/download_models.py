from django.db import models
from django_extensions.db.fields import AutoSlugField
from .language_models import Language


class Download(models.Model):
    download_id = models.AutoField(primary_key=True)

    filename = models.CharField(verbose_name="文件名",
                                max_length=255)

    date_added = models.DateTimeField(auto_now_add=True,
                                      verbose_name="添加时间")

    def __str__(self):
        return self.filename


class Download_description(models.Model):

    download = models.ForeignKey(Download,
                                 on_delete=models.CASCADE,
                                 verbose_name="下载")#这里使用多对一，备用多语言扩展
    language = models.ForeignKey(Language,
                                 on_delete=models.PROTECT,
                                 verbose_name="语言")
    name = models.CharField(verbose_name="下载名称",
                            max_length=64)

    def __str__(self):
        return self.name