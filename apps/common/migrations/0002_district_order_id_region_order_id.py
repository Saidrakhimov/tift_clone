# Generated by Django 4.2.15 on 2024-09-01 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="district",
            name="order_id",
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="region",
            name="order_id",
            field=models.IntegerField(default=11, unique=True),
            preserve_default=False,
        ),
    ]
