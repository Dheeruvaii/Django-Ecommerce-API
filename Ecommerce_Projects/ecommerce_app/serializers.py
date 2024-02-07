from rest_framework import serializers
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
    
class CartItemSerializer(serializers.ModelSerializer):
    # product_id = serializers.IntegerField()
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')

    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    # items = CartItemSerializer(many=True)  # Nested serializer for items

    class Meta:
        model = Cart
        fields = '__all__'