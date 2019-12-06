from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Product
from .forms import ProductForm


class ProductList(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'store/product_list/product_list.html'


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'store/product_detail/product_detail.html'

    def get(self, request, slug):
        form = ProductForm()
        product = get_object_or_404(Product, slug=slug)
        return render(request, self.template_name, {'form':form, 'product':product})

    def post(self, request, slug):
        form = ProductForm(request.POST)
        product = get_object_or_404(Product, slug=slug)
        if form.is_valid():
            product = get_object_or_404(Product, slug=slug)
            order = form.save(commit=False)
            order.item_name = product.item_name
            order.product_price = product.product_price
            order.first_name = form.cleaned_data['first_name']
            order.last_name = form.cleaned_data['last_name']
            order.phone_number = form.cleaned_data['phone_number']
            order.email = form.cleaned_data['email']
            order.quantity_requested = form.cleaned_data['quantity']
            order.address = form.cleaned_data['address']
            order.address_2 = form.cleaned_data['address_2']
            order.city = form.cleaned_data['city']
            order.state = form.cleaned_data['state']
            order.zip_code = form.cleaned_data['zip_code']
            order.save()

            form = ProductForm()
            return render(request, 'store/product_detail/success.html')

        args = {'form':form, 'product':product}
        return render(request, self.template_name, args)

