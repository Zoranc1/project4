from django.shortcuts import render, get_object_or_404,redirect, HttpResponse
from products.models import Product
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem, Order
from django.conf import settings
import stripe
from django.contrib import messages

stripe.api_key = settings.STRIPE_SECRET_KEY
def get_cart_item_and_total(cart):
    
    cartTotal=0
    cart_items = []
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        item_total=product.price * quantity
        
    
        cart_items.append({
            'id': product.id,
            'title': product.title,
            'description': product.content,
            'image': product.image,
            'sku': product.sku,
            'price': product.price,
            'quantity': quantity,
            'total': item_total
        })   
        cartTotal+=item_total
        
    return {'cart_items':cart_items,'cartTotal':cartTotal}
    

# Create your views here.
def checkout_show(request):
    form = MakePaymentForm()  
    order_form = OrderForm()
    
    cart = request.session.get('cart', {})
    cart_items_and_total = get_cart_item_and_total(cart)
    context = {'payment_form':form, 'order_form':order_form,'publishable': settings.STRIPE_PUBLISHABLE_KEY,}
    context.update(cart_items_and_total)

    return render(request, "checkout/checkout.html", context )


def submit_payment(request):
    cart = request.session.get('cart', {})
    cart_items_and_total = get_cart_item_and_total(cart)
    
    payment_form = MakePaymentForm(request.POST)
    order_form = OrderForm(request.POST)
    
    if order_form.is_valid() and payment_form.is_valid():
        
        #Save the Order to Database
        order = order_form.save()
        cart = request.session.get('cart',{}) 
        for product_id, quantity in cart.items():
            line_item = OrderLineItem()
            line_item.product_id = product_id
            line_item.quantity = quantity
            line_item.order = order
            line_item.save()
            
        
        #Grab the mony and run
        total = cart_items_and_total['cartTotal']
        stripe_token=payment_form.cleaned_data['stripe_id']

        try:

            total_in_cent = int(total*100)
            customer = stripe.Charge.create(
                amount=total_in_cent,
                currency="EUR",
                description="Dummy Transaction",
                card=stripe_token,
            )

        except stripe.error.CardError:
            print("Declined")
            messages.error(request, "Your card was declined!")

        if customer.paid:
            print("Paid")
            messages.error(request, "You have successfully paid")
            
            
       
        # Clear the cart        
        del request.session['cart']     
        
        return redirect('/')
def my_orders(request):
    order_line_items = OrderLineItem.objects.filter(product_id__seller=request.user,order__shipped=False).order_by('order__date')
    
    return render (request, 'checkout/my_orders.html',{'order_line_items':order_line_items})

def shipped_product(request,id):
    order = get_object_or_404(Order, pk=id)
    order.shipped =True
    order.save()
    return redirect('my_orders')
    
    
    
    
    
    
    
    
