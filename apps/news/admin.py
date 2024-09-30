from django.contrib import admin
from apps.news.models import NewsContent


@admin.register(NewsContent)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "published_time")
    list_editable = ("is_published", "published_time")

    list_filter = ("is_published",)
    exclude = ("slug",)

    search_fields = ("title", "body")
