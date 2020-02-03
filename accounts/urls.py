from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('', views.home, name="home"),
    path('dashboard', views.home, name="dashboard"),
    # CUSTOMERS
    path('customers', views.customers, name="customers"),
    path('customers/<int:customer_id>', views.customer, name='customer'),
    path('customers/add', views.addCustomer, name='add_customer'),
    path('customers/<int:customer_id>/update', views.updateCustomer, name='update_customer'),
    path('customers/<int:customer_id>/delete', views.deleteCustomer, name='delete_customer'),
    # path('customers/<int:customer_id>/orders', views.addOrder, name='add_order'),
    path('customers/<int:customer_id>/orders/add', views.addOrder, name='add_order'),
    # ORDERS
    # path('orders/add', views.addOrder, name='add_order'),
    path('orders/<int:order_id>/update', views.updateOrder, name='update_order'),
    path('orders/<int:order_id>/delete', views.deleteOrder, name='delete_order'),
    # PRODUCTS
    path('products', views.products, name="products"),
    path('products/add', views.addProduct, name="add_product"),
    path('products/<int:product_id>/update', views.updateProduct, name='update_product'),
    path('products/<int:product_id>/delete', views.deleteProduct, name='delete_product'),


    # auth urls from django.contrib.auth
    # password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset.html"
    ), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]