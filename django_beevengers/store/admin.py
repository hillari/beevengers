from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    """This class creates a better UI for the blog post dashboard"""

    list_display = ('item_name', 'product_price', 'product_quantity')
    search_fields = ['item_name', 'product_quantity']
    prepopulated_fields = {'slug': ('item_name',)}  # autofill the slug field with the title name


admin.site.register(Product, ProductAdmin)
admin.site.register(OrderRequest)
