from django.shortcuts import render


def product_view(request):
    return render(request, 'store/product_view/product_view.html')