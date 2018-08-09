from django.db import models


class Option(models.Model):
    option_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="组名",
                            max_length=64)

    def __str__(self):
        return self.name


class Option_value(models.Model):
    option_value_id = models.AutoField(primary_key=True)
    option = models.ForeignKey(Option,
                               on_delete=models.CASCADE,
                               verbose_name="选项组")

    name = models.CharField(verbose_name="选项值",
                            max_length=64)

    image = models.ImageField(upload_to="option/",
                              null=True,
                              blank=True,
                              help_text="页面展示图")

    order = models.IntegerField(default=0,
                                verbose_name="排序")

    def __str__(self):
        return self.name