from django.contrib import admin
from apps.telegram.models import TelegramModel


@admin.register(TelegramModel)
class TelegramAdmin(admin.ModelAdmin):
    list_display = ("id", "telegram_id", "first_name", "last_name", "User",)
    search_fields = ("telegram_id", "user__first_name")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
