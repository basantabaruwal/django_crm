from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Customer, Order, Tag, Product

from django.views.generic import CreateView

from .forms import OrderForm


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    orders_recent = Order.objects.order_by('-date_created')[:5]
    total_orders = orders.count()
    orders_delivered = orders.filter(status="Delivered").count()
    orders_pending = orders.filter(status="Pending").count()
    orders_cancelled = orders.filter(status="Cancelled").count()
    data = {
        'customers': customers,
        'orders': orders_recent,
        'total_orders': total_orders,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending,
        'orders_cancelled': orders_cancelled,
    }
    return render(request, 'accounts/dashboard.html', data)


def customers(request):
    customers = Customer.objects.order_by('-date_created')
    data = {
        'customers': customers
    }

    return render(request, 'accounts/customers.html', data)


def customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = customer.order_set.all()
    data = {
        'customer': customer,
        'orders': orders
    }
    return render(request, 'accounts/customer.html', data)


def products(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'accounts/products.html', data)


def register(request):
    return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')


def OrderCreateView(request):
    if request.method == 'GET':
        order_form = OrderForm()
        data = {
            'order_form': order_form
        }
        return render(request, 'accounts/order_form.html', data)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            product = form.cleaned_data['product']
            status = form.cleaned_data['status']
            # print(customer, product, status)
            # create a new order
            order = Order(customer=customer, product=product, status=status)
            order.save()
            return redirect('dashboard')

        return render(request, 'accounts/order_form.html')
