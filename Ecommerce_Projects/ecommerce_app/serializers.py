from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['name','price','descriptions','quantity']

    def to_representation(self, instance):
        """HERE PRICE AUTOMATICALLY CHANGES WITH QUANTITY PASSED"""
        representation=super().to_representation(instance)
        update_price=instance.price*instance.quantity
        representation['price']=update_price
        return representation

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class ProductCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductCategory
        fields=['product','category']


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = instance.product.name if instance.product else None
        category_data = {
            "id": instance.id,
            "item": instance.category.item  # Assuming your category field is named 'category'
        }
        representation['category'] =category_data
        return representation
    
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields =['product','quantity','created_by','created_at','updated_at']

    def validate(self, data):
        """
        Check that the quantity is not negative and does not exceed the product's available quantity.
        """
        product = data.get('product')
        quantity = data.get('quantity')

        if quantity < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")

        if product and quantity > product.quantity:
            raise serializers.ValidationError(f"Quantity exceeds available quantity for product {product}.")

        return data

   