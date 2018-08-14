from django.contrib import admin
from design.models import Banner_mode, Banner
# Register your models here.


class BannerInline(admin.TabularInline):
    model = Banner


class Banner_modeAdmin(admin.ModelAdmin):
    inlines = [BannerInline]


admin.site.register(Banner)
admin.site.register(Banner_mode, Banner_modeAdmin)