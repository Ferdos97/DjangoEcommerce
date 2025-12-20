from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin): #Class name is always uppercase
    list_display = ['id','name', 'price', 'stock']
    list_editable = ['name', 'price']
    ordering = ['id']
    # ordering = ('id',) --> Tuple

admin.site.register(Product, ProductAdmin)