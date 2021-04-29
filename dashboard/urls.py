from django.urls import path
from . import views

app_name = 'user_dashboard'

urlpatterns = [
    path('stores', views.stores, name='stores'),   
]