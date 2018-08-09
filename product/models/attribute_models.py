from django.db import models

class Attribute_group(models.Model):
    """属性组"""
    attribute_group_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="属性组",
                            max_length=64)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    """属性值"""
    attribute_id = models.AutoField(primary_key=True)
    attribute_group = models.ForeignKey(Attribute_group,
                                        on_delete=models.CASCADE,
                                        verbose_name="属性组")
    name = models.CharField(verbose_name="属性",
                            max_length=64)

    def __str__(self):
        return self.name