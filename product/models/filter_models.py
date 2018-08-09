from django.db import models

class Filter(models.Model):
    filter_id = models.AutoField(primary_key=True)
    filter_group = models.ForeignKey("Filter_group",
                                     on_delete=models.CASCADE,
                                     verbose_name="filter group")
    name = models.CharField(verbose_name="Filter key",
                            max_length=64)

    def __str__(self):
        return self.name

class Filter_group(models.Model):
    filter_group_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="filter group",
                            max_length=54)

    def __str__(self):
        return self.name