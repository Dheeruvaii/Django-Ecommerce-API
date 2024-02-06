from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter

# router=routers.DefaultRouter()
# routers.register('product',Product,basename='product'),
# routers.register('ategory',Category,basename='Category'),
# routers.register('product-category',ProductCategory,basename='product'),



urlpatterns = [
    # path('/',include('router.urls'))
    path('products/',ProductView.as_view(),name='product'),
    path('products-detail/<int:pk>/',ProductDetailView.as_view(),name='product-details'),
    path('category/',CategoryView.as_view(),name='category'),
    path('category-detail/<int:pk>/',CategoryDetailView.as_view(),name='categorydetails'),
    path('product-category/',ProductCategoryView.as_view(),name='product-category'),
    path('product-category-detail/<int:pk>/',ProductCategoryView.as_view(),name='product-category-details'),
    path('cart/', CartListView.as_view(), name='cart-detail'),
      path('add-to-cart/<int:product_id>/', AddToCart.as_view(), name='add_to_cart'),
]


    

