from django.db import models

class Language(models.Model):
    language_id = models.AutoField(primary_key=True)

    name = models.CharField(verbose_name="语言",
                            max_length=254)

    code = models.CharField(verbose_name="Code",
                            max_length=254)

    locale = models.CharField(verbose_name="当地",
                              max_length=254)

    image = models.ImageField(verbose_name="图片",
                              upload_to="language/",
                              null=True,
                              blank=True)

    sort_order = models.IntegerField(verbose_name="排序",
                                     default=0,)

    status = models.BooleanField(verbose_name="状态",
                                 default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "语言"
        verbose_name_plural = "语言"

