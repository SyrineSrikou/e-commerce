from django.urls import path
from . import views

app_name = 'discover'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name ='product_detail'),

]

    