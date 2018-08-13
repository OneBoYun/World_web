from django.db import models
from django.utils import timezone
import datetime, time
from ckeditor_uploader.fields import RichTextUploadingField
from product.models.product_models import Product
# Create your models here.
class Address(models.Model):
    """用户地址"""
    """用户地址"""
    user_id = models.IntegerField(verbose_name="用户ID")

    consignee = models.CharField(verbose_name="收件人",
                                 max_length=16)

    phone_number = models.CharField(verbose_name="手机号码",
                                   max_length=12)

    address = models.CharField(verbose_name="区域地址",
                               max_length=64)

    detailed_address = models.CharField(verbose_name="详细地址",
                                        max_length=128)


class Bill(models.Model):
    """账单"""
    genre = models.CharField(verbose_name="类型",
                             max_length=64)

    image = models.ImageField(verbose_name="图片",
                              upload_to="Bill/",
                              null=True,
                              blank=True)

    create_time = models.DateTimeField(verbose_name="创建时间",
                                       auto_now_add=True)

    name = models.CharField(verbose_name="商品名字",
                            max_length=256,
                            null=True,
                            blank=True)

    price = models.DecimalField(verbose_name="金额",
                                max_digits=19,
                                decimal_places=10)

    delete = models.BooleanField(verbose_name="删除",
                                 default=False)


class Bind_info(models.Model):
    """绑定手机"""
    user_id = models.IntegerField(verbose_name="用户ID")
    phone_number = models.CharField(verbose_name="手机号",
                                    max_length=12,
                                    null=True,
                                    blank=True)

    email = models.EmailField(verbose_name="邮箱",
                              null=True,
                              blank=True)

    real_name = models.CharField(verbose_name="真实姓名",
                                 max_length=20)

    identity_card = models.CharField(verbose_name="身份证",
                                     max_length=18)

    setpay = models.CharField(verbose_name="支付密码",
                              max_length=254,
                              null=True,
                              blank=True)


class Bonus(models.Model):
    """红包"""
    source = models.CharField(verbose_name="来源",
                              max_length=128)

    money = models.DecimalField(verbose_name="金额",
                                max_digits=9,
                                decimal_places=2)

    expiry_date = models.DateTimeField(verbose_name="有效日期",
                                       default=timezone.now() + datetime.timedelta(days=1))

    user_mode = models.BooleanField(verbose_name="领取状态",
                                    default=False)

    serial_number = models.CharField(verbose_name="流水号",
                                     default=time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + str(time.time()).replace(".", "")[-9:],
                                     max_length=32)


class Change(models.Model):
    """退换货管理"""
    name = models.CharField(verbose_name="商品名字",
                            max_length=256)

    image = models.ImageField(verbose_name="商品图片",
                              upload_to="Change/",
                              width_field=78, height_field=78,
                              null=True,
                              blank=True)

    create_time = models.DateTimeField(verbose_name="申请时间",
                                       auto_now_add=True)

    return_id = models.CharField(verbose_name="退款编号",
                                     default=time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + str(time.time()).replace(".", "")[-9:],
                                     max_length=32)

    transaction_amount = models.DecimalField(verbose_name="交易金额",
                                             max_digits=9,
                                             decimal_places=2)

    refund_amount = models.DecimalField(verbose_name="退款金额",
                                             max_digits=9,
                                             decimal_places=2)
    status_values = ((1, "退款成功"),
                     (2, "退款失败"),
                     (3, "正在退款"),
                     (4, "退款异常"))
    status = models.IntegerField(verbose_name="交易状态",
                                 choices=status_values,
                                 default=3)


class Collection(models.Model):
    """收藏夹"""
    collect_date = models.DateTimeField(verbose_name="收藏时间",
                                        auto_now_add=True)

    product_id = models.IntegerField(verbose_name="产品ID")

    name = models.CharField(verbose_name="产品名字",
                            max_length=256)

    image_url = models.CharField(verbose_name="图片链接",
                                 max_length=256)

    price = models.DecimalField(verbose_name="价格",
                                max_digits=12,
                                decimal_places=2)

    applause_rate = models.DecimalField(verbose_name="好评率",
                                        max_digits=5,
                                        decimal_places=2)

    month_sales_volume = models.IntegerField(verbose_name="月销量")


class Comment(models.Model):
    """评论"""
    user_id = models.IntegerField(verbose_name="用户ID")
    content = RichTextUploadingField(verbose_name="评价内容")
    product_id = models.IntegerField(verbose_name="商品ID")
    comment_type_values = ((1, "好评"),
                           (2, "中评"),
                           (3, "差评"))
    comment_type = models.IntegerField(verbose_name="类型",
                                       choices=comment_type_values)


class Coupon(models.Model):
    """优惠券"""
    available_date = models.DateTimeField(verbose_name="有效日期")

    price = models.IntegerField(verbose_name="面额")

    condition = models.IntegerField(verbose_name="条件金额",
                                    help_text="满指定金额才能使用")

    coupon_no = models.CharField(verbose_name="券编号",
                                     default=time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + str(time.time()).replace(".", "")[-9:],
                                     max_length=32)

    status = models.BooleanField(verbose_name="使用状态",
                                 default=False)


class Foot(models.Model):
    """浏览记录"""
    user_id = models.IntegerField(verbose_name="用户ID")
    product_id = models.IntegerField(verbose_name="浏览产品ID")
    name = models.CharField(verbose_name="产品名字",
                            max_length=254,
                            null=True,
                            blank=True)

    price = models.DecimalField(verbose_name="价格",
                                max_digits=9,
                                decimal_places=2,
                                null=True,
                                blank=True)


class Personal_information(models.Model):
    """个人信息"""
    user_id = models.IntegerField(verbose_name="用户ID")

    nickname = models.CharField("用户名",
                                max_length=64)

    real_name = models.CharField("姓名",
                                 max_length=64)

    gender_values = ((1, "男"),
                     (2, "女"),
                     (3, "未知"))
    gender = models.IntegerField(verbose_name="性别",
                                 choices=gender_values,
                                 default=3)

    birthday = models.DateField(verbose_name="生日",
                                null=True,
                                blank=True)

    phone_number = models.CharField(verbose_name="手机号码",
                                    max_length=12,
                                    null=True,
                                    blank=True)

    email = models.EmailField(verbose_name="邮箱",
                              null=True,
                              blank=True)


class Order(models.Model):
    """订单"""
    user_id = models.IntegerField(verbose_name="用户ID")

    product_id = models.IntegerField(verbose_name="商品ID")

    address_id = models.IntegerField(verbose_name="地址ID")

    logistics_id = models.IntegerField(verbose_name="物流单号")

    order_status_values = ((1, "待付款"),
                           (2, "待发货"),
                           (3, "待收获"),
                           (4, "待评价"))
    order_status = models.IntegerField(verbose_name="订单状态",
                                       choices=order_status_values,
                                       default=1)

    detail_schedule_values = ((1, "拍下商品"),
                              (2, "卖家发货"),
                              (3, "确认收货"),
                              (4, "交易完成"))
    detail_schedule = models.IntegerField(verbose_name="详情进度",
                                          choices=detail_schedule_values)

    order_no = models.CharField(verbose_name="流水号",
                                default=time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + str(time.time()).replace(".", "")[-9:],
                                max_length=32)

    create_datetime = models.DateTimeField(verbose_name="交易日期",
                                           auto_now_add=True)

    price = models.DecimalField(verbose_name="单价",
                                max_digits=9,
                                decimal_places=2)

    number = models.IntegerField(verbose_name="数量",
                                 default=1)

    transaction_status_values = ((1,"交易成功"),
                                 (2, "交易关闭"),
                                 (3, "买家已付款"),
                                 (4, "卖家已发货"),
                                 (5, "退款"),
                                 (6, "退款/退货"))
    transaction_status = models.IntegerField(verbose_name="交易状态",
                                             choices=transaction_status_values)

    operation = models.BooleanField(verbose_name="交易操作",
                                    default=False,
                                    help_text="删除订单")


class Changing_or_Refunding_apply(models.Model):
    """退换货申请"""
    user_id = models.IntegerField(verbose_name="用户ID")
    product_id =models.IntegerField(verbose_name="商品ID")

    return_type = models.IntegerField(verbose_name="退款类型",
                                      choices=((1, "仅退款"),
                                               (2, "退货退款")),
                                      default=1)

    return_cause = models.IntegerField(verbose_name="退款原因",
                                       choices=((1, "不想要了"),
                                                (2, "买错了"),
                                                (3, "没收到货"),
                                                (4, "与说明不符"),
                                                (5, "其他")),
                                       default=1
                                       )

    return_price = models.DecimalField(verbose_name="退款金额",
                                       max_digits=9,
                                       decimal_places=2)

    return_explain = models.CharField(verbose_name="退款说明",
                                      max_length=254)


class return_goods_image(models.Model):
    """退货图片"""
    return_id = models.ForeignKey(Changing_or_Refunding_apply,
                                  verbose_name="退货申请ID",
                                  on_delete=models.CASCADE,
                                  )
    evidence = models.ImageField(verbose_name="上传凭证",
                                 upload_to="return_goods_images/")