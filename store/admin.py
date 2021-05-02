from django.contrib import admin
from .models import Store, Category, Product, ProductImage
class StoreAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner','logo']

admin.site.register(Store,StoreAdmin)
admin.site.register([Product, ProductImage])



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
