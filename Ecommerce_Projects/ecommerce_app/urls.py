from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('Products',ProductView.as_view(),name='product-details')
]
