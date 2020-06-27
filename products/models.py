from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    discount = models.FloatField()

    def __str__(self):
        return self.code


class ProductSelected(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)  # user specify korlam
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quanity = models.IntegerField(default=1)
    order = models.BooleanField(default=False)
