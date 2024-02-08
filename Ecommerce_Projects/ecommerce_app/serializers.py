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
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')
    class Meta:
        model = Cart
        fields =['product','quantity','created_by','product_id','created_at','updated_at']

    def validate(self, data):
        product = data['product']
        cart = data['cart']

        # Check product quantity
        if product.quantity < cart.quantity:
            raise serializers.ValidationError("Product quantity is insufficient.")

        # Check cart capacity
        cart_items_count = Cart.objects.filter(cart=cart).count()
        if cart_items_count >= cart.capacity:
            raise serializers.ValidationError("Cart capacity exceeded.")

        return data