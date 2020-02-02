from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    def number_of_orders(self):
        return self.order_set.count()

    class Meta:
        ordering = ('-date_created',)


class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=30, null=True, choices=CATEGORY)
    description = models.TextField(null=True)
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS, default=STATUS[0])
