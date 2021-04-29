from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('create_store/', views.createStore, name='create_store'),
]