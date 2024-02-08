from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics,status
from rest_framework.viewsets import ModelViewSet
from .filters import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from django.shortcuts import get_object_or_404
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_data={
            'message':" object created successfully",
            'data':serializer.data
        }
        return Response(response_data, status=201)
    

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'message': "Users-list",
            'data': serializer.data
        })


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'message': "Object retrieved successfully",
            'data': serializer.data
        })
    

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': "Object updated successfully",
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ProductFilter
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({
            'message' : "object created successfully",
            'data' : serializer.data
        })
    
    def list(self,request,*args):
        data=self.filter_queryset(self.get_queryset())
        serializer=self.get_serializer(data,many=True)
        return Response({
            'message':"Products-Lists",
            'data' : serializer.data
        })
    
    def retrieve(self, request, *args, **kwargs):
        data=self.get_object()
        serializer=self.get_serializer(data)
        return Response({
            'message':"retrieved object",
            'data' : serializer.data
        }) 
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            
            'message': 'updated instance',
            'data' : super().update(request, *args, **kwargs)
        }) 
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({
            'message' : "object created successfully",
            'data' : serializer.data
        })
    
    def list(self,request,*args):
        data=self.filter_queryset(self.get_queryset())
        serializer=self.get_serializer(data,many=True)
        return Response({
            'message':"Category-Lists",
            'data' : serializer.data
        })
    
    def retrieve(self, request, *args, **kwargs):
        data=self.get_object()
        serializer=self.get_serializer(data)
        return Response({
            'message':"retrieved object",
            'data' : serializer.data
        }) 
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            
            'message': 'updated instance',
            'data' : super().update(request, *args, **kwargs)
        }) 
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializers

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({
            'message' : "object created successfully",
            'data' : serializer.data
        })
    
    def list(self,request,*args):
        data=self.filter_queryset(self.get_queryset())
        serializer=self.get_serializer(data,many=True)
        return Response({
            'message':"Products-Category-Lists",
            'data' : serializer.data
        })
    
    def retrieve(self, request, *args, **kwargs):
        data=self.get_object()
        serializer=self.get_serializer(data)
        return Response({
            'message':"retrieved object",
            'data' : serializer.data
        }) 
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            
            'message': 'updated instance',
            'data' : super().update(request, *args, **kwargs)
        }) 
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({
                'message' : "object created successfully",
                'data' : serializer.data
                    })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self,request,*args):
        data=self.filter_queryset(self.get_queryset())
        serializer=self.get_serializer(data,many=True)
        return Response({
            'message':"Cart-Lists",
            'data' : serializer.data
        })
    
    def retrieve(self, request, *args, **kwargs):
        data=self.get_object()
        serializer=self.get_serializer(data)
        return Response({
            'message':"retrieved object",
            'data' : serializer.data
        }) 
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            
            'message': 'updated instance',
            'data' : super().update(request, *args, **kwargs)
        }) 
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
