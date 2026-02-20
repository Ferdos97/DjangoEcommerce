import uuid 
from django.db import models
from accounts.models import CustomUser

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2) # ---> max digit number includes decimal.
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} $ {self.price}"

class ContactUs(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Contact Us'

class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='order')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Orders'


class OrderItems(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='items')
    amount = models.PositiveIntegerField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Order Items'

