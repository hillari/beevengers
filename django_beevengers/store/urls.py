from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('<slug:slug>/', views.ProductDetail.as_view(), name='product_detail')
    #path('product_list/', views.product_list, name='product_list'),

]