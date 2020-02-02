import django_filters
from .models import Product, Order
from django import forms

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'tags']


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'date_created', 'status']