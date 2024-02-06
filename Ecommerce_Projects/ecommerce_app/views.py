from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from django.shortcuts import get_object_or_404
# Create your views here.
class ProductView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    filter_backends=[DjangoFilterBackend]
    filterset_class=ProductFilter


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

    def retrieve(self, request,pk, *args, **kwargs):
        data=Product.objects.get(pk=pk)
        update_price=data.price*data.quantity
        data.price=update_price
        serializer=ProductSerializers(data)
        return Response(serializer.data)    # def list(self,request):
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

# class AddToCartAPIView(APIView):
#     def post(self, request, product_id):
#         product = Product.objects.get(pk=product_id)
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#         cart_item.quantity += 1
#         cart_item.save()
#         serializer = CartSerializer(cart)
#         return Response(serializer.data)

# class RemoveFromCartAPIView(APIView):
#     def post(self, request, product_id):
#         product = Product.objects.get(pk=product_id)
#         cart = Cart.objects.get(user=request.user)
#         cart_item = CartItem.objects.get(cart=cart, product=product)
#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1
#             cart_item.save()
#         else:
#             cart_item.delete()
#         serializer = CartSerializer(cart)
#         return Response(serializer.data)


class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    

     
class AddToCart(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)