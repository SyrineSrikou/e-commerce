from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('create_store/', views.createStore, name='create_store'),
    path('store/<int:store_id>', views.store, name='store_dashboard'),
    path('store/<int:store_id>/products', views.store_products, name='store_products'),
    path('store/<int:store_id>/add_product', views.add_product, name='add_product'),

]