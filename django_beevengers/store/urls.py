from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product-list')
    #path('product_view/', views.product_view, name='product_view'),

]