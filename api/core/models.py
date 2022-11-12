from itertools import product
from unicodedata import category
from django.db import models

    
class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()
    description = models.TextField(max_length=100)
    category = models.ManyToManyField("Category")
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    