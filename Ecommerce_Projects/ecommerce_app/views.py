from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ProductView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    # def list(self,request):
    #     return super().self.objects.all()

    # def create(self, request, *args, **kwargs):
    #     serializers=ProductSerializers(many=True,data=request.data)
    #     serializers.is_valid()
    #     serializers.save
    #     return Response(serializers.data)