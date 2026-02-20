from django.contrib import admin
from .models import Product, ContactUs, Order, OrderItems



class OrderItemInline(admin.TabularInline):
    model = OrderItems
    extra = 1

# stack


class ProductAdmin(admin.ModelAdmin): #Class name is always uppercase
    list_display = ['id','name', 'price', 'stock']
    list_editable = ['name', 'price']
    ordering = ['id']
    # ordering = ('id',) --> Tuple



class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id','fullname', 'email', 'message']
    ordering = ['id']


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id','user']
    ordering = ['id']

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['id']
    ordering = ['id']


admin.site.register(Product, ProductAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)
