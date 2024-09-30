from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime

from apps.common.models import District
from apps.education.models import Direction

User = get_user_model()


class Gender(models.TextChoices):
    MALE = 'Male', 'Erkak'
    FEMALE = 'Famele', 'Ayol'


class Application(models.Model):
    class ApplicationChoose(models.TextChoices):
        ACCEPTED = "accepted", "qabul qilindi"
        REJECTED = "rejected", "rad etildi"

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    passport = models.CharField(max_length=9)
    pinf = models.CharField(max_length=14)
    gender = models.CharField(max_length=6, choices=Gender.choices)
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=12, choices=ApplicationChoose.choices)
    birth_date = models.DateField()
    faculty = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs) -> None:
        from weasyprint import HTML
        from django.conf import settings
        import os

        if (
                self.status == self.ApplicationChoose.ACCEPTED or self.status == self.ApplicationChoose.REJECTED) and not self.accepted_at:
            if self.status == self.ApplicationChoose.ACCEPTED:
                if not os.path.exists("contracts"):
                    os.makedirs("contracts")
                    file_name = f"contracts/{self.first_name}-{self.last_name}.pdf"
                    HTML(f"{settings.HOST_NAME}{reverse('application-generator')}?application_id=(self.pk)").write_pdf(
                        file_name)
                    self.contract_url = file_name
            self.accepted_at = datetime.now()

        return super().save(*args, **kwargs)
