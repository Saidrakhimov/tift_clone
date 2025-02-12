# Generated by Django 4.2.15 on 2024-09-04 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("common", "0003_social_alter_district_options_alter_region_options"),
        ("education", "0003_direction"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("passport", models.CharField(max_length=9)),
                ("pinf", models.CharField(max_length=14)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Erkak"), ("Famele", "Ayol")], max_length=6
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("accepted", "qabul qilindi"),
                            ("rejected", "rad etildi"),
                        ],
                        max_length=12,
                    ),
                ),
                ("birth_date", models.DateField()),
                ("faculty", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("accepted_at", models.DateTimeField()),
                (
                    "direction",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="education.direction",
                    ),
                ),
                (
                    "district",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="common.district",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
