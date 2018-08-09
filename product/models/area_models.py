from django.db import models

class Province(models.Model):
    """省份直辖区"""
    province_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="省/直辖市/特别行政区",
                            max_length=10, help_text="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "省份直辖区"
        verbose_name_plural = "省份直辖区"


class City(models.Model):
    """城市"""
    city_id = models.AutoField(primary_key=True)
    province = models.ForeignKey(Province,
                                 verbose_name="省份",
                                 on_delete=models.CASCADE)
    name = models.CharField(verbose_name="城市",
                            max_length=5,
                            help_text="包括地级市/县级市/自治区直辖县级市")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = "城市"


class Municipal_district(models.Model):
    """市辖区"""
    municipal_district_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City,
                             verbose_name="城市",
                             on_delete=models.CASCADE,
                             help_text="直辖区，县级市")