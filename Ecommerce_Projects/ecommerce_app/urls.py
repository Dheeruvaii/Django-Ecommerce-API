from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('products',ProductView.as_view(),name='product-details'),
    path('category/',CategoryView.as_view(),name='category'),
    path('product-category/',CategoryView.as_view(),name='product-category'),

    
]
