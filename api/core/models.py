from itertools import product
from unicodedata import category
from django.db import models

    
class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()
    value = models.FloatField(null=True)
    description = models.TextField(max_length=100)
    category = models.ManyToManyField("Category")
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Transaction(models.Model):
    code = models.IntegerField()
    status = models.CharField(max_length=30)
    value = models.FloatField(null=True)
    product = models.ManyToManyField("Product")
    
class Contato(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=200)

