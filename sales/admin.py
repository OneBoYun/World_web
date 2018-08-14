from django.contrib import admin
from .models import Sale_type, Sales
# Register your models here.

class SaleInline(admin.TabularInline):
    model = Sales


class Sales_typeAdmin(admin.ModelAdmin):
    inlines = [SaleInline,]


admin.site.register(Sale_type, Sales_typeAdmin)
admin.site.register(Sales)
