import django_filters
from .models import *
from rest_framework import request


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name']

   

# class CartFilter(django_filters.FilterSet):
#     assign = django_filters.CharFilter(lookup_expr='icontains') 
#     class Meta:
#         model=Cart
#         fields= ['assign']
