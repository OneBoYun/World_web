from django.db import models
from .language_models import Language
from .area_models import Province, City
from .attribute_models import Attribute
from .customer_models import Customer_group
from .filter_models import Filter
from .option_models import Option_value
from .category_models import Category
from .download_models import Download
from django.utils import timezone
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from sales.models import Sales
# Create your models here.

class Manufacturer(models.Model):
    """厂家/制造商"""
    name = models.CharField(max_length=64,
                            verbose_name="厂家/制造商")
    image = models.ImageField(upload_to="Manufacturer/",
                              null=True,
                              blank=True,
                              verbose_name="logo")
    sort_order = models.IntegerField(default=0,
                                     verbose_name="排序",
                                     help_text="数字越小，则排序越靠前")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "厂家/制造商"
        verbose_name_plural = "厂家/制造商"


class Product(models.Model):
    """模型需联合查看"""
    product_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=256,
                            default="",
                            verbose_name="默认商品名字",
                            help_text="其他国家可以在详情选择填写")

    model = models.CharField(verbose_name="型号",
                             max_length=64)

    sku = models.CharField(verbose_name="SKU",
                           max_length=64,
                           null=True,
                           blank=True)

    upc = models.CharField(verbose_name="UPC",
                           max_length=12,
                           null=True,
                           blank=True)#UPC码商品条码是用来表示UCC-12商品标识代码的条码符号，是由美国统一代码委员会（UCC）制定的一种条码码制，主要用于美国和加拿大地区，我们在美国进口的商品上可以看到。

    ean = models.CharField(verbose_name="EAN",
                           max_length=14,
                           null=True,
                           blank=True)#EAN码是国际物品编码协会制定的一种商品用条码，通用于全世界。EAN码符号有标准版（EAN-13）和缩短版（EAN-8）两种。标准版表示13位数字，又称为EAN13码，缩短版表示8位数字，又称EAN8。两种条码的最后一位为校验位，由前面的12位或7位数字计算得出。

    jan = models.CharField(verbose_name="JAN",
                           max_length=13,
                           null=True,
                           blank=True)#JAN CODE 是 Japanese Article Number Code的缩写，是日本通用商品编码。JAN CODE和条形码类似，用以保证商品的质量与来源正当。

    isbn = models.CharField(verbose_name="ISBN",
                            max_length=17,
                            null=True,
                            blank=True)#国际标准书号（英语：International Standard Book Number，缩写为ISBN），是国际通用的图书或独立的出版物（定期出版的期刊除外）代码。出版社可以通过国际标准书号清晰地辨认所有非期刊书籍。一个国际标准书号只有一个或一份相应的出版物与之对应。一本书的每一版或其他的变化，能够申请到一个新的国际标准书号。新版本如果在原来旧版的基础上没有内容上太大的变动，在出版时不会得到新的国际标准书号。当一本书同时有平装本与精装本出版时，平装本的国际标准书号不得用于精装本，反之亦然。
    mpn = models.CharField(verbose_name="MPN",
                           max_length=64,
                           null=True,
                           blank=True)#在电子外贸中 MPN（Manufacturing Part Number）制造方编号。
    location = models.ForeignKey(City,
                                on_delete=models.SET_NULL,
                                verbose_name="区域",
                                null=True,
                                blank=True,
                                 help_text="指定商品在某一个地区显示，不指定则全部显示")#指定商品在某一个地区显示，不指定则全部显示

    quantity = models.IntegerField(verbose_name="库存",
                                   null=True,
                                   blank=True,
                                   default=1000)

    stock_status_id = models.IntegerField(verbose_name="商铺id",
                                          default=0,
                                          null=True,
                                          blank=True)#0代表属于系统商铺, 商家发布商品，自动添加商品ID

    image = models.ImageField(verbose_name="主图",
                              upload_to="product_image/",
                              null=True,
                              blank=True)

    manufacturer_id = models.ForeignKey(Manufacturer,
                                        null=True,
                                        blank=True,
                                        verbose_name="生产厂家",
                                        on_delete=models.SET_NULL)

    shipping = models.BooleanField(verbose_name="运送",
                                   default=True)

    price = models.DecimalField(verbose_name="价格",
                                max_digits=19,
                                decimal_places=10,
                                null=True,
                                blank=True)

    tax_class_id = models.IntegerField(verbose_name="税收",
                                       null=True,
                                       blank=True,
                                       default=0)

    date_available = models.DateField(verbose_name="可用日期",
                                      default=timezone.now)#默认当天发布日期，设置成未来的日期，则在未来预定那天显示

    weight = models.DecimalField(verbose_name="重量",
                                 max_digits=19,
                                 decimal_places=10,
                                 null=True,
                                 blank=True)
    Weight_Class = (
        ("Kilogram", "公斤"),
        ("Gram", "公克"),
        ("Pound", "磅 "),
        ("Ounce", "盎司"),
    )
    weight_class_id = models.CharField(verbose_name="重量单位",
                                       max_length=8,
                                       choices=Weight_Class,
                                       default="Kilogram")

    length = models.DecimalField(verbose_name="长",
                                 max_digits=19,
                                 decimal_places=10,
                                 null=True,
                                 blank=True)

    width = models.DecimalField(verbose_name="宽",
                                 max_digits=19,
                                 decimal_places=10,
                                 null=True,
                                 blank=True)

    height = models.DecimalField(verbose_name="高",
                                max_digits=19,
                                decimal_places=10,
                                null=True,
                                blank=True)

    Length_Class = (
        ("Centimeter", "厘米"),
        ("Millimeter", "毫米"),
        ("Inch", "英寸")
    )

    length_class_id = models.CharField(verbose_name="长度单位",
                                       max_length=10,
                                       choices=Length_Class,
                                       default="Centimeter")

    sort_order = models.IntegerField(verbose_name="商品排序",
                                     default=0,
                                     null=True,
                                     blank=True)

    status = models.BooleanField(verbose_name="商品状态",
                                 default=True)#判断是否在前端显示

    viewed = models.IntegerField(verbose_name="浏览量",
                                 default=0,
                                 null=True,
                                 blank=True)
    sales_volume = models.IntegerField(verbose_name="销量",
                                       default=0,
                                       null=True,
                                       blank=True)

    date_added = models.DateTimeField(verbose_name="添加日期",
                                      auto_now_add=True)

    date_modified = models.DateTimeField(verbose_name="修改日期",
                                         auto_now=True)

    class Meta:
        db_table = 'world_product'
        verbose_name = "商品"
        verbose_name_plural = "商品"
        app_label = "product"#兼容1.7以前版本

    def __str__(self):
        return str(self.model)


class Product_attribute_value(models.Model):
    """商品属性值"""
    product_attribute_value_id = models.AutoField(primary_key=True)

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="商品")

    attribute_key = models.ForeignKey(Attribute,
                                      on_delete=models.CASCADE,
                                      verbose_name="属性值")
    text = models.CharField(verbose_name="文本",
                            max_length=100)

    def __str__(self):
        return str(self.attribute_key) + "---" + self.text

    class Meta:
        verbose_name = "属性"
        verbose_name_plural = "属性"


class Product_description(models.Model):
    """商品详情-分离是为了对接多国语言"""
    product_description_id = models.AutoField(primary_key=True)

    language = models.ForeignKey(Language,
                                 on_delete=models.CASCADE,
                                 verbose_name="国家/地区-语言")

    product = models.OneToOneField(Product,
                                   on_delete=models.CASCADE,
                                   verbose_name="商品详情")

    name = models.CharField(verbose_name="商品名称",
                            max_length=254)
    description = RichTextUploadingField(verbose_name="商品详情",
                                   null=True,
                                   blank=True)

    tag = models.CharField(verbose_name="标签",
                           null=True,
                           blank=True,
                           max_length=254)

    meta_title = models.CharField(verbose_name="Meta Title",
                                  null=True,
                                  blank=True,
                                  max_length=254)

    meta_description = models.TextField(verbose_name="Meta Description",
                                        null=True,
                                        blank=True)

    meta_keyword = models.CharField(verbose_name="Meta Keyword",
                                    null=True,
                                    blank=True,
                                    max_length=254)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "详情"
        verbose_name_plural = "详情"


class Product_discount(models.Model):
    """商品折扣"""
    product_discount_id = models.AutoField(primary_key=True)

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="商品折扣")

    price = models.DecimalField(max_digits=19,
                                decimal_places=9,
                                verbose_name="价格",
                                default=0,
                                help_text="默认为0，则表示没有折扣")

    customer = models.OneToOneField(Customer_group,
                                 on_delete=models.CASCADE,
                                 verbose_name="客户组")

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = "商品折扣"
        verbose_name_plural = "商品折扣"


class Product_filter(models.Model):
    """商品过滤"""
    product_filter_id = models.AutoField(primary_key=True)
    filter = models.ForeignKey(Filter,
                               on_delete=models.CASCADE,
                               verbose_name="filter")
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="商品")
    text = models.CharField(max_length=64,
                            verbose_name="过滤关键字 ",
                            default="")

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "商品过滤"
        verbose_name_plural = "商品过滤"


class Product_image(models.Model):
    """商品附属图"""
    product_image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="商品")
    image = models.ImageField(upload_to="product_image/",
                              verbose_name="商品图")

    order = models.IntegerField(default=0,
                                verbose_name="排序")

    def __str__(self):
        return str(self.product_image_id)

    class Meta:
        verbose_name = "商品附属图"
        verbose_name_plural = "商品附属图"


class Product_option(models.Model):
    """商品选项"""
    product_option_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="商品")
    option_value = models.ForeignKey(Option_value,
                                     on_delete=models.CASCADE,
                                     verbose_name="选项值")

    name = models.CharField(max_length=64,
                            verbose_name="型号名")

    image= models.ImageField(upload_to="option/",
                             null=True,
                             blank=True,
                             verbose_name="选项图")

    quantity = models.IntegerField(default=0,
                                   verbose_name="库存",
                                   null=True,
                                   blank=True)

    subtract = models.BooleanField(verbose_name="Subtract Stock",
                                   default=True,
                                   help_text="是否支持使用优惠券，默认支持")
    price = models.DecimalField(verbose_name="Price",
                                max_digits=19,
                                decimal_places=10)

    integral = models.IntegerField(verbose_name="积分",
                                   null=True,
                                   blank=True,
                                   default=0,
                                   help_text="1积分等于RMB一元，客户可用于积分抵扣")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "商品选项"
        verbose_name_plural = "商品选项"


class Product_related(models.Model):
    """相关联商品"""
    product_related = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="商品",
                                related_name="product")

    related_name = models.ForeignKey(Product,
                                    on_delete=models.CASCADE,
                                    related_name="related_product",
                                    verbose_name="关联商品",
                                    max_length=256)

    order = models.IntegerField(default=0,
                                verbose_name="排序")

    related_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.related_name)

    class Meta:
        verbose_name = "相关联商品"
        verbose_name_plural = "相关联商品"


class Product_Special(models.Model):
    """VIP特价"""
    special_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="商品")
    customer_group = models.ForeignKey(Customer_group,
                                       on_delete=models.CASCADE,
                                       verbose_name="VIP客户群体")
    priority = models.IntegerField(verbose_name="优先级",
                                   default=0)
    price = models.IntegerField(verbose_name="折扣百分比%",
                                help_text="原价的减去折扣百分比")
    Date_start = models.DateTimeField(verbose_name="开始时间",
                                      default=timezone.now)
    Date_end = models.DateTimeField(verbose_name="结束时间",
                                    default=timezone.now)

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = "特价"
        verbose_name_plural = "特价"


class Product_category(models.Model):
    """产品分类"""
    product = models.OneToOneField(Product,
                                   on_delete=models.CASCADE,
                                   verbose_name="商品")
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name="分类")

    def __str__(self):
        return str(self.product) + str(self.category)

    class Meta:
        verbose_name = "产品分类"
        verbose_name_plural = "产品分类"


class Product_download(models.Model):
    """下载商品数据"""
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="商品")
    download = models.ForeignKey(Download,
                                 on_delete=models.PROTECT,
                                 verbose_name="下载")#启动models。PROTECT保护，防止误删除

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = "下载商品数据"
        verbose_name_plural = "下载商品数据"


class Product_activity(models.Model):
    sales_id = models.ForeignKey(Sales,
                              on_delete=models.CASCADE,
                              verbose_name="活动名称")
    product_id = models.OneToOneField(Product,
                                      on_delete=models.CASCADE,
                                      )
    price = models.DecimalField(verbose_name="活动价",
                                max_digits=9,
                                decimal_places=2)