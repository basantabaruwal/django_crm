from django.forms import ModelForm
from .models import Order, Product, Customer, Tag

class OrderForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(OrderForm, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.id:
    #         self.fields['customer'].widget.attrs['readonly'] = True

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


class FilterForm(ModelForm):
    class Meta:
        model = Product
        fields=['name','price','category','description','tags']