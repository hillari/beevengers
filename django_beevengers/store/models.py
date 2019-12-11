from django.db import models
from datetime import datetime


class Product(models.Model):
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    product_image = models.ImageField(upload_to='images/store_images')
    slug = models.SlugField(max_length=100, unique=True)

    # 6 allows price up to $9,999.99
    product_price = models.DecimalField(default=1.99, max_digits=6, decimal_places=2)
    product_quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item_name


class OrderRequest(models.Model):
    order_date = models.DateTimeField(default=datetime.now)
    item_name = models.CharField(max_length=200, default=None)
    product_price = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField(max_length=30, default="")
    phone_number = models.CharField(max_length=200, default=None)
    email = models.EmailField(max_length=70, blank=True, null=True)
    quantity_requested = models.CharField(max_length=100, default=None)
    address = models.CharField(max_length=200, default=None)
    address_2 = models.CharField(max_length=200, blank=True, default=None)
    city = models.CharField(max_length=200, default=None)
    state = models.CharField(max_length=200, default=None)
    zip_code = models.IntegerField(default=None)

    def __str__(self):
        return self.first_name + " " + self.last_name

