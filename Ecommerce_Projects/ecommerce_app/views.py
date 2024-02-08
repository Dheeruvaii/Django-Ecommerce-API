from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics,status
from rest_framework.viewsets import ModelViewSet
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
            'message': "Object retrieved successfully",
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

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
    
    # def update(self, request, *args, **kwargs):
    #     return Response({
            
    #         'message': 'updated instance',
    #         'data' : super().update(request, *args, **kwargs)
    #     }) 
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializers

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


# # class AddToCartAPIView(APIView):
# #     def post(self, request, product_id):
# #         product = Product.objects.get(pk=product_id)
# #         cart, created = Cart.objects.get_or_create(user=request.user)
# #         cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
# #         cart_item.quantity += 1
# #         cart_item.save()
# #         serializer = CartSerializer(cart)
# #         return Response(serializer.data)

# # class RemoveFromCartAPIView(APIView):
# #     def post(self, request, product_id):
# #         product = Product.objects.get(pk=product_id)
# #         cart = Cart.objects.get(user=request.user)
# #         cart_item = CartItem.objects.get(cart=cart, product=product)
# #         if cart_item.quantity > 1:
# #             cart_item.quantity -= 1
# #             cart_item.save()
# #         else:
# #             cart_item.delete()
# #         serializer = CartSerializer(cart)
# #         return Response(serializer.data)


# class CartListView(generics.ListCreateAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)


# class AddToCart(generics.CreateAPIView):
#     serializer_class = CartItemSerializer

#     def create(self, request, *args, **kwargs):
#         # Check if 'product_id' is present in request.data
#         if 'product_id' in request.data:
#             # If 'product_id' is present, initialize the serializer with the expected fields
#             serializer = self.get_serializer(data=request.data)
#         else:
#             # If 'product_id' is not present, add it to the request data
#             request_data_with_product_id = request.data.copy()
#             request_data_with_product_id['product_id'] = request.data.get('product')
#             serializer = self.get_serializer(data=request_data_with_product_id)

#         # Continue with serializer validation and response handling as before
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
