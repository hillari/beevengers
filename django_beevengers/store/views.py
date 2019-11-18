from django.shortcuts import render
from django.views import generic
from .models import Product


class ProductList(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'store/product_view/product_list.html'


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'store/product_view/product_detail.html'


# def model_image_upload(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)

# def product_view(request):
#     return render(request, 'store/product_view/product_list.html')
