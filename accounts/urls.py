from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('', views.home, name="home"),
    path('dashboard', views.home, name="dashboard"),
    path('products', views.products, name="products"),
    path('customers', views.customers, name="customers"),
    path('customers/<int:customer_id>', views.customer, name='customer'),
    path('orders/add', views.OrderCreateView, name='add_order'),
]