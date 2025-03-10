from django.db import models

# Create your models here.

class Feature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    features = models.TextField()
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.question

class DemoRequest(models.Model):
    ROBOT_STATUS_CHOICES = [
        ('has_bot', 'ربات دارم'),
        ('no_bot', 'ربات ندارم'),
    ]

    mobile = models.CharField(max_length=15, verbose_name='شماره موبایل')
    telegram_id = models.CharField(max_length=100, verbose_name='آیدی تلگرام')
    email = models.EmailField(verbose_name='ایمیل')
    panel_name = models.CharField(max_length=100, verbose_name='نام پنل')
    panel_version = models.CharField(max_length=20, verbose_name='نسخه پنل')
    robot_status = models.CharField(
        max_length=10,
        choices=ROBOT_STATUS_CHOICES,
        default='no_bot',
        verbose_name='وضعیت ربات'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    class Meta:
        verbose_name = 'درخواست دمو'
        verbose_name_plural = 'درخواست‌های دمو'
        db_table = 'demo_requests'

    def __str__(self):
        return f"{self.panel_name} - {self.mobile}"
