from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'carts', CartViewSet)


urlpatterns = [
      path('',include(router.urls)),
#     path('products/',ProductView.as_view(),name='product'),
#     path('products-detail/<int:pk>/',ProductDetailView.as_view(),name='product-details'),
#     path('category/',CategoryView.as_view(),name='category'),
#     path('category-detail/<int:pk>/',CategoryDetailView.as_view(),name='categorydetails'),
#     path('product-category/',ProductCategoryView.as_view(),name='product-category'),
#     path('product-category-detail/<int:pk>/',ProductCategoryView.as_view(),name='product-category-details'),
#     path('cart/', CartListView.as_view(), name='cart-detail'),
#       path('add-to-cart/<int:product_id>/', AddToCart.as_view(), name='add_to_cart'),
]


    

