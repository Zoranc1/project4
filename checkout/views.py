from django.shortcuts import render, get_object_or_404,redirect, HttpResponse
from adds.models import Ad
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
import stripe
from django.contrib import messages

stripe.api_key = settings.STRIPE_SECRET_KEY
def get_cart_item_and_total(cart):
    
    cartTotal=0
    cart_items = []
    
    for ad_id, quantity in cart.items():
        ad = get_object_or_404(Ad, pk=ad_id)
        item_total=ad.price * quantity
        
    
        cart_items.append({
            'id': ad.id,
            'title': ad.title,
            'description': ad.content,
            'image': ad.image,
            'sku': ad.sku,
            'price': ad.price,
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
        for ad_id, quantity in cart.items():
            line_item = OrderLineItem()
            line_item.ad_id = ad_id
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
    order_line_items = OrderLineItem.objects.filter(ad_id__seller=request.user)
    
    return render (request, 'checkout/my_orders.html',{'order_line_items':order_line_items})

