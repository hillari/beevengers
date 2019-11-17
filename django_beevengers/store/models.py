from django.db import models
import os


# def get_image_path():
#     return os.path.join('photos', str(instance.id), filename)
#
class Product(models.Model):
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    product_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.item_name

