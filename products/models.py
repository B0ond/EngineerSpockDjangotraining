from django.db import models

# Create your models here.
# model == таблица бд


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(Null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(Null=True, blank=True)
