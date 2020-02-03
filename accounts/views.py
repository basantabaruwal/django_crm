from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from crm_django.decorators.decorators import not_for_authenticated_user
from django.contrib import messages

from .models import Customer, Order, Tag, Product

# from django.views.generic import CreateView
from django.forms import inlineformset_factory


from .forms import OrderForm, ProductForm, CustomerForm, TagForm, FilterForm

from .filters import OrderFilter


@login_required(login_url='login')
def home(request):
    # # print("**********USER: ", request.user)
    # if not request.user.is_authenticated:
    #     # user not authorized to view this page
    #     # return redirect(request.META['HTTP_REFERER'])
    #     return redirect('login')
    # # otherwise continue
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

    orderFilter = OrderFilter(request.GET, queryset=orders)
    orders = orderFilter.qs

    data = {
        'customer': customer,
        'orders': orders,
        'filter': orderFilter
    }
    return render(request, 'accounts/customer.html', data)


def addCustomer(request):
    if request.method == "GET":
        form = CustomerForm()
        data = {
            'form': form,
            'action_btn_name': 'Add Customer'
        }
        return render(request, 'accounts/customer_form.html', data)

    if request.method=="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            customer_name = form.cleaned_data['name']
            messages.info(request, "Customer '{}' is successfully added.".format(customer_name))
            return redirect('customers')


def updateCustomer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == "GET":
        form = CustomerForm(instance=customer)
        data = {
            'form': form,
            'action_btn_name': 'Add Customer'
        }

        return render(request, 'accounts/customer_form.html', data)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.info(request, "Customer updated successfully")
            return redirect('customers')


def deleteCustomer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == "POST":
        customer.delete()

        messages.info(request, "Customer removed successfully")
        return redirect('customers')

    return redirect(request.META['HTTP_REFERER'])


def addOrder(request, customer_id):
    # print("******************Customer ID: ", customer_id)

    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status',), extra=1)
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'GET':
        # order_form = OrderForm(
        #     initial = {
        #         'customer': customer
        #     }
        # )

        formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

        data = {
            # 'form': order_form,
            'formset': formset,
            'action_btn_name': 'Place Order(s)',
            'customer': customer,
        }
        return render(request, 'accounts/order_form.html', data)

    if request.method == 'POST':
        print("***************REQUEST: ", request.method)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            # customer = form.cleaned_data['customer']
            # product = form.cleaned_data['product']
            # status = form.cleaned_data['status']
            # # print(customer, product, status)
            # # create a new order
            # order = Order(customer=customer, product=product, status=status)
            # order.save()
            formset.save()
            messages.info(request, "Order(s) placed successfully")
            return redirect('dashboard')

    return redirect(request.META['HTTP_REFERER'])


def updateOrder(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    customer = order.customer
    if request.method == 'GET':
        order_form = OrderForm(instance=order)
        data = {
            'form': order_form,
            'action_btn_name': 'Update Order',
            # 'customer': customer,
        }
        return render(request, 'accounts/order_form.html', data)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.info(request, "Order updated successfully")
            return redirect('dashboard')

        return render(request, 'accounts/order_form.html')


def deleteOrder(request, order_id):
    print("***********REQUEST METHOD************** ", request.method)
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=order_id)
        order.delete()
        messages.info(request, "Order removed successfully")
        return redirect(request.META['HTTP_REFERER'])


    return redirect('customers')


def products(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'accounts/products.html', data)


def addProduct(request):
    if request.method == 'GET':
        form = ProductForm()
        data = {
            'form': form,
            'action_btn_name': 'Add Product',
        }

        return render(request, 'accounts/product_form.html', data)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Product added successfully")
            return redirect('products')


    return redirect(request.META['HTTP_REFERER'])


def updateProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        data = {
            'form': form,
            'action_btn_name': 'Update Product',
        }

        return render(request, 'accounts/product_form.html', data)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, "Product updated successfully")
            return redirect('products')

    return redirect(request.META['HTTP_REFERER'])


def deleteProduct(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        messages.info(request, "Product deleted successfully")
        return redirect('products')

    return redirect(request.META('HTTP_REFERER'))




def register(request):
    # print("**********USER: ", request.user)
    if request.user.is_authenticated:
        # user not authorized to view this page
        # return redirect(request.META['HTTP_REFERER'])
        return redirect('dashboard')

    # otherwise continue
    if request.method=="GET":
        return render(request, 'accounts/register.html')

    if request.method=="POST": 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        data = {
            'values': request.POST,
        }
        #check if the username is already taken
        if User.objects.filter(username=username).exists():
            # username is already taken
            messages.warning(request, "Username '{}' is already taken!".format(username))
            return render(request, 'accounts/register.html', data)
        elif User.objects.filter(email=email).exists():
            # username is available
            # check for duplicate email
            # but the email is duplicate
            messages.warning(request, "User with email '{}' is already registered!".format(email))
            return render(request, 'accounts/register.html', data)
        elif password != password_confirm:
            # passwords do not match
            messages.warning(request, "Passwords do not match")
            return render(request, 'accounts/register.html', data)
        else:
            # everything looks good
            # create the user
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)

            messages.warning(request, "Thank you for registering. Please login to proceed.")
            return redirect('login')


@not_for_authenticated_user
def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    if request.method=="POST":
        # check if the user exists
        username = request.POST['username']
        password = request.POST['password']
        print("username {}  and password {}.".format(username, password))
        data = {
            'values': request.POST,
        }
        user = auth.authenticate(username=username, password=password)
        if user is None:
            # Invalid Credentials
            messages.error(request, "Invalid Credentials!")
            return render(request, 'accounts/login.html', data)
        else:
            # user exists, proceed to login
            auth.login(request, user)
            messages.success(request, "Welcome to dashboard")
            return redirect('dashboard')


@login_required(login_url="login")
def logout(request):
    # # print("**********USER: ", request.user)
    # if not request.user.is_authenticated:
    #     # user not authorized to view this page
    #     # return redirect(request.META['HTTP_REFERER'])
    #     return redirect('login')
    # # otherwise continue
    if request.method=="GET":
        return redirect(request.META['HTTP_REFERER'])

    if request.user.is_authenticated and request.method=="POST":
        auth.logout(request)
        messages.info(request, "You're now logged out.")
        return redirect('login')
