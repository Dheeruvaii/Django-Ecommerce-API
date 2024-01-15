from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    descriptions=models.CharField(max_length=50)
    quantity=models.IntegerField()
    # image=models.ImageField(default='img.png')

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
    items = models.ManyToManyField(Product, through='CartItem')


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)