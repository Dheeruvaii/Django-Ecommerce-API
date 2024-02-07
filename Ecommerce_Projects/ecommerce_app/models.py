from django.db import models

# Create your models here."""

class User(models.Model):
    """THIS IS TEMPORARY USER MODEL .USER DATA COMES FROM AUTHENTICATIONS APP"""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    descriptions=models.CharField(max_length=50)
    quantity=models.IntegerField()
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    item=models.CharField(max_length=30)
    # descriptions=models.CharField(max_length=50)


    def __str__(self):
        return self.item
    

class ProductCategory(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

class Cart(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # items = models.ManyToManyField('CartItem', related_name='carts')
    items=models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    