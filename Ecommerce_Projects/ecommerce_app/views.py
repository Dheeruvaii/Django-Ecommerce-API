from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
# Create your views here.
class ProductView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    filter_backends=[DjangoFilterBackend]
    filterset_class=ProductFilter


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    # def list(self,request):
    #     return super().self.objects.all()

    # def create(self, request, *args, **kwargs):
    #     serializers=ProductSerializers(many=True,data=request.data)
    #     serializers.is_valid()
    #     serializers.save
    #     return Response(serializers.data)

class CategoryView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers


class ProductCategoryView(generics.ListCreateAPIView):
    queryset=ProductCategory.objects.all()
    serializer_class=ProductCategorySerializers



class ProductCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=ProductCategory.objects.all()
    serializer_class=ProductCategorySerializers
