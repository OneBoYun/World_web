from django.db import models
from django.conf import settings

class Customer_activity(models.Model):
    customer_activity_id = models.AutoField(primary_key=True)

    key = models.CharField(verbose_name="KEY",
                           null=True,
                           blank=True,
                           max_length=128)

    data = models.CharField(verbose_name="DATA",
                            null=True,
                            blank=True,
                            max_length=254)

    ip = models.GenericIPAddressField(verbose_name="IP",
                                      null=True,
                                      blank=True)

    date_added = models.DateTimeField(verbose_name="添加时间",
                                      auto_now_add=True)


class Customer_affiliate(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_id = models.AutoField(primary_key=True)
    Customer_activity = models.OneToOneField(Customer_activity,
                                             null=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name="客户足迹")
    customer_group = models.ForeignKey("Customer_group",
                                       null=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name="客户组")

    company = models.CharField(verbose_name="公司",
                               null=True,
                               blank=True,
                               max_length=254)

    email = models.EmailField(verbose_name="邮箱",
                              null=True,
                              blank=True)

    website = models.URLField(verbose_name="站点",
                              null=True,
                              blank=True)

    tracking = models.CharField(verbose_name="Tracking code",
                                null=True,
                                blank=True,
                                max_length=64)

    commission = models.IntegerField(verbose_name="佣金",
                                     default=5)

    bank_name = models.CharField(verbose_name="银行",
                                 null=True,
                                 blank=True,
                                 max_length=64)

    bank_account_name = models.CharField(verbose_name="银行账户名称",
                                         null=True,
                                         blank=True,
                                         max_length=64)

    bank_account_number = models.IntegerField(verbose_name="银行帐号码",
                                              null=True,
                                              blank=True)

    status = models.BooleanField(verbose_name="启用/关闭",
                                 default=True)

    date_added = models.DateTimeField(auto_now_add=True)

    create_ip = models.GenericIPAddressField(verbose_name="IP地址",
                                             null=True,
                                             blank=True,
                                             editable=False)

    integral = models.IntegerField(verbose_name="积分",
                                   null=True,
                                   blank=True)


class Customer_group(models.Model):
    """客户组"""
    customer_group = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="客户组",
                            max_length=64)
    description = models.CharField(verbose_name="描述",
                                   null=True,
                                   blank=True,
                                   max_length=254)

    def __str__(self):
        return self.name

