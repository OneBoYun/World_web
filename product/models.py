# from django.db import models
# from django.utils import timezone
# # Create your models here.
#
# class Manufacturer(models.Model):
#     pass
#
# class Product(models.Model):
#     """模型需联合查看"""
#     product_id = models.AutoField(primary_key=True)
#
#     model = models.CharField(verbose_name="型号",
#                              max_length=64)
#
#     sku = models.CharField(verbose_name="SKU",
#                            max_length=64,
#                            null=True,
#                            blank=True)
#
#     upc = models.CharField(verbose_name="UPC",
#                            max_length=12,
#                            null=True,
#                            blank=True)#UPC码商品条码是用来表示UCC-12商品标识代码的条码符号，是由美国统一代码委员会（UCC）制定的一种条码码制，主要用于美国和加拿大地区，我们在美国进口的商品上可以看到。
#
#     ean = models.CharField(verbose_name="EAN",
#                            max_length=14,
#                            null=True,
#                            blank=True)#EAN码是国际物品编码协会制定的一种商品用条码，通用于全世界。EAN码符号有标准版（EAN-13）和缩短版（EAN-8）两种。标准版表示13位数字，又称为EAN13码，缩短版表示8位数字，又称EAN8。两种条码的最后一位为校验位，由前面的12位或7位数字计算得出。
#
#     jan = models.CharField(verbose_name="JAN",
#                            max_length=13,
#                            null=True,
#                            blank=True)#JAN CODE 是 Japanese Article Number Code的缩写，是日本通用商品编码。JAN CODE和条形码类似，用以保证商品的质量与来源正当。
#
#     isbn = models.CharField(verbose_name="ISBN",
#                             max_length=17,
#                             null=True,
#                             blank=True)#国际标准书号（英语：International Standard Book Number，缩写为ISBN），是国际通用的图书或独立的出版物（定期出版的期刊除外）代码。出版社可以通过国际标准书号清晰地辨认所有非期刊书籍。一个国际标准书号只有一个或一份相应的出版物与之对应。一本书的每一版或其他的变化，能够申请到一个新的国际标准书号。新版本如果在原来旧版的基础上没有内容上太大的变动，在出版时不会得到新的国际标准书号。当一本书同时有平装本与精装本出版时，平装本的国际标准书号不得用于精装本，反之亦然。
#     mpn = models.CharField(verbose_name="MPN",
#                            max_length=64,
#                            null=True,
#                            blank=True)#在电子外贸中 MPN（Manufacturing Part Number）制造方编号。
#     location = models.ForeignKey('self',
#                                 on_delete=models.CASCADE,
#                                 verbose_name="区域",
#                                 null=True,
#                                 blank=True)#指定商品在某一个地区显示，不指定则全部显示
#
#     quantity = models.IntegerField(verbose_name="库存",
#                                    null=True,
#                                    blank=True,
#                                    default=1000)
#
#     stock_status_id = models.IntegerField(verbose_name="商铺id",
#                                           default=0,
#                                            null=True,
#                                           blank=True)#0代表属于系统商铺, 商家发布商品，自动添加商品ID
#
#     image = models.ImageField(verbose_name="主图",
#                               upload_to="product_image",
#                               null=True,
#                               blank=True)
#
#     manufacturer_id = models.ForeignKey(Manufacturer,
#                                         null=True,
#                                         blank=True,
#                                         verbose_name="生产厂家",
#                                         on_delete=models.SET_NULL)
#
#     shipping = models.BooleanField(verbose_name="运送",
#                                    default=True)
#
#     price = models.DecimalField(verbose_name="价格",
#                                 max_digits=19,
#                                 decimal_places=10,
#                                 null=True,
#                                 blank=True)
#
#     Promotion_Rate = models.DecimalField(verbose_name="促销价",
#                                          max_digits=19,
#                                          decimal_places=10,
#                                          null=True,
#                                          blank=True)
#
#     tax_class_id = models.IntegerField(verbose_name="税收",
#                                        null=True,
#                                        blank=True,
#                                        default=0)
#
#     date_available = models.DateField(verbose_name="可用日期",
#                                       default=timezone.now)#默认当天发布日期，设置成未来的日期，则在未来预定那天显示
#
#     weight = models.DecimalField(verbose_name="重量",
#                                  max_digits=19,
#                                  decimal_places=10,
#                                  null=True,
#                                  blank=True)
#     Weight_Class = (
#         ("Kilogram", "公斤"),
#         ("Gram", "公克"),
#         ("Pound", "磅 "),
#         ("Ounce", "盎司"),
#     )
#     weight_class_id = models.CharField(verbose_name="重量单位",
#                                        max_length=8,
#                                        choices=Weight_Class,
#                                        default="Kilogram")
#
#     length = models.DecimalField(verbose_name="长",
#                                  max_digits=19,
#                                  decimal_places=10,
#                                  null=True,
#                                  blank=True)
#
#     width = models.DecimalField(verbose_name="宽",
#                                  max_digits=19,
#                                  decimal_places=10,
#                                  null=True,
#                                  blank=True)
#
#     height = models.DecimalField(verbose_name="高",
#                                 max_digits=19,
#                                 decimal_places=10,
#                                 null=True,
#                                 blank=True)
#
#     Length_Class = (
#         ("Centimeter", "厘米"),
#         ("Millimeter", "毫米"),
#         ("Inch", "英寸")
#     )
#
#     length_class_id = models.CharField(verbose_name="长度单位",
#                                        max_length=10,
#                                        choices=Length_Class,
#                                        default="Centimeter")
#
#     sort_order = models.IntegerField(verbose_name="商品排序",
#                                      default=0,
#                                      null=True,
#                                      blank=True)
#
#     status = models.BooleanField(verbose_name="商品状态",
#                                  default=True)#判断是否在前端显示
#
#     viewed = models.IntegerField(verbose_name="浏览量",
#                                  default=0,
#                                  null=True,
#                                  blank=True)
#
#     date_added = models.DateTimeField(verbose_name="添加日期",
#                                       auto_now_add=True)
#
#     date_modified = models.DateTimeField(verbose_name="修改日期",
#                                          auto_now=True)
#
#     class Meta:
#         db_table = 'world_product'
#         verbose_name = "商品"
#         verbose_name_plural = "商品"
#
#     def __str__(self):
#         return self.model
#
#
