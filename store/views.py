from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . import models, forms
from .forms import *
from .models import Store, Product, ProductImage
from django.contrib.auth.models import User
from django.utils.text import slugify



# Open a Store
def createStore(request):
    store=models.Store.objects.filter(owner=request.user)
    form = CreateStoreForm()
    if request.method == 'POST':
        form = CreateStoreForm(request.POST, request.FILES)
        if form.is_valid():
            storeForm = form.save(commit=False)
            storeForm.owner=request.user
            storeForm.store_created=True
            storeForm.save()
            form.save()
            store = form.cleaned_data.get('title')
            return redirect('user_dashboard:stores')

    context = {'form':form, 'store':store}
    return render(request, 'create_store.html', context)


#get specific store by Id
def store(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    context = {
        'store' : store
    }
    return render(request, 'store_dashboard.html', context)


def add_product(request, store_id):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        store = get_object_or_404(Store, pk=store_id)
        if form.is_valid():
            product = form.save(commit=False)
            product.added_by = store
            product.slug = slugify(product.title)
            product.save()
            images = request.FILES.getlist("more_images")
            for i in images:
                ProductImage.objects.create(product=product, image=i)

            return redirect('discover:home')
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})

def store_products(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    products = Product.objects.all()
    store_products = products.filter(pk=store_id)
   
    context = {
        'store':store,
        'store_products': store_products,
        'products' : products
    }
    return render(request, 'store_products.html', context)