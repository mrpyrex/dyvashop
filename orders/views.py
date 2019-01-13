from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart
from pypaystack import Transaction, Customer, Plan
from django.conf import settings

def order_create(request):
    cart        = Cart(request)
    if request.method == 'POST':
        form    = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, 
                                            product=item['product'], 
                                            price=item['price'], 
                                            quantity=item['quantity'])
            cart.clear()
            order_created.delay(order.id)
            request.session['order_id'] = order.id

            # context = {
            #     'order':order,
            #     'data_key':data_key,
            #     'paystack_total':paystack_total
            # }
            return render(request, 'orders\order\created.html')

    else:
        form = OrderCreateForm()
    return render(request, 'orders\order\create.html', {'cart': cart, 'form': form})