from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .models import *



class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
 
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='store_owner')
    title = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, upload_to='stores/logos/')
    store_created=models.BooleanField(default=False)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='Stores'

    def logo_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.logo.url))
    logo_tag.short_description = 'Logo'
   

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_by = models.ForeignKey(Store, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    warranty = models.CharField(max_length=300, null=True, blank=True)
    return_policy = models.CharField(max_length=300, null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return self.product.title




