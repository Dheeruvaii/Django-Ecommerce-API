from django.contrib import admin
from .models import User, Product, Category, ProductCategory, Cart

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'descriptions', 'quantity', 'is_available', 'created_at', 'modified_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('item',)

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass  # No special configuration needed for this model

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_by', 'created_at', 'updated_at')