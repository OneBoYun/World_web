from django.db import models
from .filter_models import Filter
from .language_models import Language
import pymysql.cursors

# Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='user',
#                              password='passwd',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# try:
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()

# import sqlite3
# conn = sqlite3.connect("/home/zhangbo/桌面/World_web/db.sqlite3")
# cursor = conn.cursor()
# cursor.execute('select * from product_category_description where category_id=')
# values = cursor.fetchall()

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=256,
                            default="",
                            verbose_name="分类名字",
                            help_text="其他语言可在详情填写")

    image = models.ImageField(upload_to="category/",
                              null=True,
                              blank=True,
                              verbose_name="图片")

    parend = models.ForeignKey("self",
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               verbose_name="父类")

    top = models.BooleanField(verbose_name="置顶",
                              help_text="只适用顶层分类",
                              default=False)
    column = models.IntegerField(verbose_name="子分类",
                                 help_text="拥有多少层子分类",
                                 default=1)

    sort_order = models.IntegerField(verbose_name="排序",
                                     default=0)

    status = models.BooleanField(verbose_name="ON/OFF",
                                 help_text="开启或者关闭分类",
                                 default=True)

    date_added = models.DateTimeField(verbose_name="添加日期",
                                      auto_now_add=True)

    date_mofified = models.DateTimeField(verbose_name="修改日期",
                                         auto_now=True)

    def __str__(self):
        # import sqlite3
        # conn = sqlite3.connect("/home/zhangbo/桌面/World_web/db.sqlite3")
        # cursor = conn.cursor()
        # cursor.execute('select * from product_category_description where category_id=?', (self.category_id,))
        # values = cursor.fetchall()
        # # for i in values:
        # #     return i[1]
        # cursor.close()
        # conn.close()
        # try:
        #     return values[0][1]
        # except:
        #     return ""
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"


class Category_description(models.Model):
    """多语言接入"""
    category_description_id = models.AutoField(primary_key=True)

    category = models.OneToOneField(Category,
                                    on_delete=models.CASCADE,
                                    verbose_name="分类")

    language_id = models.ForeignKey(Language,
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True,
                                    verbose_name="语言",
                                    help_text="提供不同语言针对不同国家")

    name = models.CharField(verbose_name="类名",
                            max_length=255)

    description = models.TextField(verbose_name="详情",
                                   null=True,
                                   blank=True)

    meta_title = models.CharField(verbose_name="META TITLE",
                                  null=True,
                                  blank=True,
                                  max_length=255)

    meta_description = models.CharField(verbose_name="META TITLE",
                                  null=True,
                                  blank=True,
                                  max_length=255)

    meta_keyword = models.CharField(verbose_name="META KEYWORD",
                                    null=True,
                                    blank=True,
                                    max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类详情"
        verbose_name_plural = "分类详情"


class Category_filter(models.Model):
    category_filter_id = models.AutoField(primary_key=True)
    filter = models.ForeignKey(Filter,
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name="过滤标签")
    category = models.OneToOneField(Category,
                                    on_delete=models.CASCADE,
                                    verbose_name="分类")

    def __str__(self):
        return self.category_filter_id

    class Meta:
        verbose_name = "分类筛选"
        verbose_name_plural = "分类筛选"