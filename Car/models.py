from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name_category = models.CharField(max_length=230)


class CarOnline(models.Model):
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prise = models.IntegerField(blank=True, null=True)
    years = models.IntegerField(blank=True, null=True)
    date_create = models.DateField(auto_now_add=True, null=True, blank=True)
    number_phone = models.CharField(max_length=230)


class ReviewCom(models.Model):
    review = models.TextField()
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(CarOnline, on_delete=models.CASCADE)

    def __str__(self):
        return self.review
