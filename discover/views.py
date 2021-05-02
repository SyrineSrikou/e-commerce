from django.shortcuts import render, get_object_or_404
from store.models import Product

def home(request):
    products = Product.objects.all()[0:8]

    return render(request, 'home.html', {'products': products})


def product_detail(request, category_slug, product_slug):
   
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    return render(request, 'product_detail.html', {'product': product} )
