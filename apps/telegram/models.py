from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TelegramModel(models.Model):
    telegram_id = models.BigIntegerField()
    User = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
