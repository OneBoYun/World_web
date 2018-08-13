from django.contrib import admin
from information.models import (Address, Bill, Bind_info, Bonus, Change, Collection,
                                Comment, Coupon, Foot, Personal_information, Order,
                                Changing_or_Refunding_apply, return_goods_image)
# Register your models here.
admin.site.register(Address)
admin.site.register(Bill)
admin.site.register(Bind_info)
admin.site.register(Bonus)
admin.site.register(Change)
admin.site.register(Collection)
admin.site.register(Comment)
admin.site.register(Coupon)
admin.site.register(Foot)
admin.site.register(Personal_information)
admin.site.register(Order)
admin.site.register(Changing_or_Refunding_apply)
admin.site.register(return_goods_image)