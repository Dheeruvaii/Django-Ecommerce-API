"""
Handle PaymentL:
                To handle payment, you can use a third-party payment gateway like Stripe or PayPal.
                  Here’s an example of how to integrate Stripe with Django:
                `First, install the Stripe Python library:
                                                        1.pip install stripe
                                                        2.STRIPE_SECRET_KEY = 'your_stripe_secret_key'
                                                        3.views.py code
import stripe
from django.conf import settings
from django.shortcuts import render, redirect

def payment_process(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(
                amount=1000,
                currency='usd',
                description='Example charge',
                source=token,
            )
            # Handle successful payment
            return redirect('success')
        except stripe.error.CardError as e:
            # Handle failed payment
            return redirect('failure')
    return render(request, 'payment.html')

If you don't want to use HTML templates for handling payments,
you can use Django's built-in form handling and process the payments entirely on the server side.
Here's an example of how you can modify the previous code to handle payments without HTML templates:

                Install the Stripe Python library:

                Copy
                pip install stripe
                Set up your Stripe account and obtain the necessary API keys.

                In your Django project settings, add the Stripe API keys:

                python
                Copy
                # settings.py

                STRIPE_PUBLIC_KEY = 'your_stripe_public_key'
                STRIPE_SECRET_KEY = 'your_stripe_secret_key'
                Create a view for processing payments. Here's an example using Stripe:

                python
                Copy
                # views.py

                import stripe
                from django.conf import settings
                from django.views import View
                from django.http import JsonResponse

                stripe.api_key = settings.STRIPE_SECRET_KEY

                class PaymentView(View):
                    def post(self, request):
                        # Retrieve the cart and total amount

                        try:
                            intent = stripe.PaymentIntent.create(
                                amount=total_amount_in_cents,
                                currency='usd',
                                payment_method_types=['card'],
                                metadata={'cart_id': cart.id}
                            )
                            client_secret = intent.client_secret
                            return JsonResponse({'client_secret': client_secret})
                        except stripe.error.CardError as e:
                            return JsonResponse({'error': str(e)})
Update your URL patterns to include the payment processing view.

# urls.py

                        from django.urls import path
                        from .views import PaymentView

                        urlpatterns = [
                            # Other URL patterns
                            path('process-payment/', PaymentView.as_view(), name='process_payment'),
                        ]
                            """

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