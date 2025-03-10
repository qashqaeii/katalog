# Generated by Django 5.1.7 on 2025-03-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DemoRequest",
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
                (
                    "mobile",
                    models.CharField(max_length=15, verbose_name="شماره موبایل"),
                ),
                (
                    "telegram_id",
                    models.CharField(max_length=100, verbose_name="آیدی تلگرام"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="ایمیل")),
                (
                    "panel_name",
                    models.CharField(max_length=100, verbose_name="نام پنل"),
                ),
                (
                    "panel_version",
                    models.CharField(max_length=20, verbose_name="نسخه پنل"),
                ),
                (
                    "robot_status",
                    models.CharField(
                        choices=[("has_bot", "ربات دارم"), ("no_bot", "ربات ندارم")],
                        default="no_bot",
                        max_length=10,
                        verbose_name="وضعیت ربات",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت"),
                ),
            ],
            options={
                "verbose_name": "درخواست دمو",
                "verbose_name_plural": "درخواست\u200cهای دمو",
                "db_table": "demo_requests",
            },
        ),
    ]
