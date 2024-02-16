import django_filters
from .models import *
from rest_framework import request


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains') 

    class Meta:
        model = Product
        fields = ['name']

   

# class TaskFilter(django_filters.FilterSet): 
#     task_name = django_filters.CharFilter(lookup_expr='icontains')  
#     due = django_filters.CharFilter(lookup_expr='icontains')
#     class Meta:
#         model = Task
#         fields = ['due','task_name']
   
