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
