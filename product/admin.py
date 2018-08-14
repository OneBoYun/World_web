from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.core import serializers
from django.http import HttpResponse

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _

from product.models.area_models import (Province,City,Municipal_district)
from product.models.attribute_models import (Attribute_group, Attribute)
from product.models.category_models import (Category, Category_description, Category_filter)
from product.models.customer_models import (Customer_activity, Customer_affiliate, Customer_group)
from product.models.download_models import (Download, Download_description)
from product.models.filter_models import (Filter, Filter_group)
from product.models.language_models import Language
from product.models.option_models import (Option, Option_value)
from product.models.product_models import (Manufacturer, Product, Product_attribute_value, Product_description,
                                           Product_discount, Product_filter, Product_image,
                                           Product_option, Product_related, Product_Special,
                                           Product_category, Product_download, Product_activity)

# Register your models here.





from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'Product admin'


admin_site = MyAdminSite(name='myadmin')
admin_site.register(Product)


class BasicAdminSite(AdminSite):
    site_header = 'Basic admin'


basic_site = BasicAdminSite(name='BasicAdmin')
basic_site.register(Product)


class AdvancedAdminSite(AdminSite):
    site_header = 'Advanced admin'


advanced_site = AdvancedAdminSite(name='AdvancedAdmin')
advanced_site.register(Product)


def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response
export_as_json.short_description = "导出JSON"
admin.site.add_action(export_as_json)

def export_selected_objects(modeladmin, request, queryset):#还未写各种导出格式处理视图
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))
export_selected_objects.short_description = "导出"
admin.site.add_action(export_selected_objects)

#admin.site.disable_action('delete_selected')#禁用删除选项


class AttributeInline(admin.TabularInline):
    model = Product_attribute_value
    max_num = 10



class DescriptionInline(admin.TabularInline):
    model = Product_description


class DiscountInline(admin.TabularInline):
    model = Product_discount


class FilterInline(admin.TabularInline):
    model = Product_filter


class ImageInline(admin.TabularInline):
    model = Product_image


class OptionInline(admin.TabularInline):
    model = Product_option


class RelatedInline(admin.TabularInline):
    model = Product_related
    fk_name = "product"


class SpecialInline(admin.TabularInline):
    model = Product_Special


class CategoryInline(admin.TabularInline):
    model = Product_category


class DownloadInline(admin.TabularInline):
    model = Product_download


class ActivityInline(admin.TabularInline):
    model = Product_activity


def upper_case_name(obj):
    """设置后添加到list_display"""
    return ("%s %s" % (obj.model, obj.sku)).upper()
upper_case_name.short_description = 'Name'


class ManufacturerAdmin(admin.ModelAdmin):
    ordering = ['sort_order']
    search_fields = ["name", "sort_order"]#搜索域


class CityAdmin(admin.ModelAdmin):
    ordering = ["province"]
    search_fields = ["province", "name"]


class ProductAdmin(admin.ModelAdmin):
    # actions = None
    show_full_result_count = False #设置show_full_result_count为控制是否应在过滤的管理页面上显示完整的对象计数
    search_fields = ["name", "product_id", "model", "sku", "quantity", "status", "viewed"] #商品列表搜索框
    save_on_top = True #商品编辑页面顶部保存按钮
    #raw_id_fields = ("manufacturer_id", "location")#默认情况下，Django的管理员使用选择框界面（<select>）作为字段ForeignKey。有时您不希望产生必须选择要在下拉列表中显示的所有相关实例的开销。
    autocomplete_fields = ['manufacturer_id', 'location']#添加外键搜索框 商品编辑页使用
    date_hierarchy = "date_added"
    list_display = ["name", "product_id", "model", "sku", "status", "date_added", "quantity", ]#设置list_display控制在管理员的更改列表页面上显示的字段
    list_display_links = ["name", "product_id", "model", "sku", "status", "date_added", ]#将字段赋予超链接
    list_editable = ["quantity",]#在列表页赋予可编辑状态
    list_filter = ["model", "sku", "status", "quantity",] #设置list_filter为激活管理员更改列表页面右侧边栏中的过滤器
    list_per_page = 15 #设置每页显示的条数
    ordering = ["product_id",]#根据指定字段排序
    # radio_fields = {"manufacturer_id": admin.VERTICAL}
    fieldsets = (
        ("属性", {
            'fields': ("name", ("image", "location"),
                       ("price", 'model', 'sku'),
                       ("upc", "ean", "jan", "isbn", "mpn"),
                       ("length_class_id", "height", "width", "length"),
                       ("weight_class_id", "weight"),
                       ("sales_volume", "viewed", "sort_order", "tax_class_id", "stock_status_id", "quantity"),
                       ("date_available", "manufacturer_id", "status", "shipping"))
        }),
    )
    # fields = (("image", "location"),
    #           ("price", 'model', 'sku'),
    #           ("upc", "ean", "jan", "isbn", "mpn"),
    #           ("length_class_id", "height", "width", "length"),
    #           ("weight_class_id", "weight"),
    #           ("viewed", "sort_order", "tax_class_id", "stock_status_id", "quantity"),
    #           ("date_available", "manufacturer_id", "status", "shipping"))#商品编辑页

    readonly_fields = ["viewed", "sales_volume"]#设置为只读

    inlines = [ActivityInline,
        AttributeInline, DescriptionInline, DiscountInline, FilterInline,
        OptionInline, ImageInline, RelatedInline, SpecialInline,
        CategoryInline, DownloadInline,
    ]
    actions = ["Close_status", "Batch_shelves"]#批量上下架商品

    def Batch_shelves(self, request, queryset):
        rows_updated = queryset.update(status=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    Batch_shelves.short_description = "上架商品"

    def Close_status(self, request, queryset):
        rows_updated = queryset.update(status=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    Close_status.short_description = "下架商品"

    actions_on_top = True #顶部菜单选项True为开启
    actions_on_bottom = True #底部菜单选项True为开启
    actions_selection_counter = True #控制是否在操作下拉列表旁显示选择计数器。默认情况下，管理员更改列表将显示它
    empty_value_display = 'empty' #替换默认显示空值方法


class DescriptionAdmin(admin.ModelAdmin):
    list_display = ["name", "product_description_id", "language", "tag"]


class CategoryAdmin(admin.ModelAdmin):
    # list_display = ('name', 'image_data')
    readonly_fields = ('image_data',)

    def image_data(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.image.url)

    image_data.short_description = '分类图片'# 页面显示的字段名称



admin.site.register(Province)
admin.site.register(City, CityAdmin)
admin.site.register(Municipal_district)

admin.site.register(Attribute_group)
admin.site.register(Attribute)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Category_description)
admin.site.register(Category_filter)

admin.site.register(Customer_activity)
admin.site.register(Customer_affiliate)
admin.site.register(Customer_group)

admin.site.register(Download)
admin.site.register(Download_description)

admin.site.register(Filter)
admin.site.register(Filter_group)

admin.site.register(Language)

admin.site.register(Option)
admin.site.register(Option_value)

admin.site.register(Product, ProductAdmin)
admin.site.register(Product_attribute_value)
admin.site.register(Product_description, DescriptionAdmin)
admin.site.register(Product_discount)
admin.site.register(Product_filter)
admin.site.register(Product_image)
admin.site.register(Product_option)
admin.site.register(Product_related)
admin.site.register(Product_Special)
admin.site.register(Product_category)
admin.site.register(Product_download)
admin.site.register(Manufacturer, ManufacturerAdmin)


class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)