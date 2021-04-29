from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('create_store/', views.createStore, name='create_store'),
    path('store/<int:store_id>', views.store, name='store_dashboard'),

]