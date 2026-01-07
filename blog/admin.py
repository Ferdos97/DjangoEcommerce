from django.contrib import admin
from .models import Product
from .models import ContactUs

class ProductAdmin(admin.ModelAdmin): #Class name is always uppercase
    list_display = ['id','name', 'price', 'stock']
    list_editable = ['name', 'price']
    ordering = ['id']
    # ordering = ('id',) --> Tuple

admin.site.register(Product, ProductAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id','fullname', 'email', 'message']
    ordering = ['id']

admin.site.register(ContactUs, ContactUsAdmin)
