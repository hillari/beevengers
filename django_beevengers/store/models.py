from django.db import models
import os


# def get_image_path():
#     return os.path.join('photos', str(instance.id), filename)
#
class Product(models.Model):
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    product_image = models.ImageField(upload_to='images/')
    # 6 allows price up to $9,999.99
    product_price = models.DecimalField(default=1.99, max_digits=6, decimal_places=2)
    product_quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item_name

