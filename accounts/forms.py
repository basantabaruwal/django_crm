from django.forms import ModelForm
from .models import Order, Product, Customer, Tag

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'tags']



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'email', 'phone']



class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']