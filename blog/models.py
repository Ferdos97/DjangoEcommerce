from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2) # ---> max digit number includes decimal.
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)