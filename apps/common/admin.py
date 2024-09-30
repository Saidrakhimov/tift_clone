from django.contrib import admin
from apps.common.models import *


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'order_id']
    list_editable = ['order_id']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'order_id', 'get_region_title', ]
    list_editable = ['order_id']

    def get_region_title(self, obj):
        return obj.region.title


@admin.register(Social)
class SocialModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'social', 'link']
    list_editable = ['title', 'social', 'link']
