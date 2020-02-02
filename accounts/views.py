from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):
    return render(request, 'accounts/products.html')


def customer(request):
    return render(request, 'accounts/customer.html')


def register(request):
    return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')