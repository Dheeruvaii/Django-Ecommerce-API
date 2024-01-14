from rest_framework import serializers
from .models import *



class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class ProductCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductCategory
        fields='__all__'
