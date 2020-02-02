from django.contrib import admin
from .models import Customer, Product, Order, Tag

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'date_created')
    list_display_links = ('name', 'email')
    list_filter = ('name', 'email', 'address', 'date_created')
    list_per_page = 20
    search_fields = ('name','address', 'date_created')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    list_display_links= ('name',)
    list_filter = ('name', 'price', 'category',)
    list_per_page = 20
    search_fields = ('name' 'price', 'category', 'description',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'date_created', 'note')
    list_filter = ('status',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tag)
