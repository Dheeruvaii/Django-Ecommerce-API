# from django.shortcuts import get_list_or_404
# from django.contrib.sessions.models import Session
# from .models import Product

# class Cart:
#     def __init__(self,request):
#         self.session = request.session
#         cart=self.session.get('cart')
#         if 'cart' not in self.session:
#             cart=self.session['cart']={}
#         self.cart=cart

#     def add_product(self,product_id,quantity):
#         product=get_list_or_404(Product,pk=product_id)
#         if product_id not in self.cart:
#             self.cart[product_id]={'quantity':quantity,'price':product.price}     
#         else:
#             self.cart[product_id] += quantity

#         self.save()

#     def remove_product(self,product_id):
#         if product_id in self.cart:
#             del self.cart[product_id]
#             self.save()

#     def update_quantity(self,product_id,quantity):
#         self.cart[product_id]=quantity
#         self.save()


#     def get_cart_items(self):
#         product_ids = self.cart.keys()
#         products = Product.objects.filter(pk__in=product_ids)
#         return [(product, self.cart[str(product.id)]['quantity']) for product in products]

#     def clear_cart(self):
#         self.session.pop('cart', None)

#     def get_cart_total(self):
#         total = sum(item['price'] * item['quantity'] for item in self.cart.values())
#         return total

#     def save(self):
#         self.session.modified = True

#         """
#         views.py

        

# from django.shortcuts import get_object_or_404,redirect
# from .cart import Cart

# def add_to_cart(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, pk=product_id)
#     cart.add_product(product_id, quantity=1)
#     return redirect('cart')

# def remove_from_cart(request, product_id):
#     cart = Cart(request)
#     cart.remove_product(product_id)
#     return redirect('cart')

# def update_cart(request, product_id):
#     cart = Cart(request)
#     quantity = int(request.POST['quantity'])
#     cart.update_quantity(product_id, quantity)
#     return redirect('cart')

# def view_cart(request):
#     cart = Cart(request)
#     cart_items = cart.get_cart_items()
#     cart_total = cart.get_cart_total()
#     return render(request, 'cart.html', {'cart_items': cart_items, 'cart_total': cart_total})

#         """