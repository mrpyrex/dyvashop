from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from orders.models import Order
from cart.cart import Cart
from pypaystack import Transaction, Customer, Plan
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')

@csrf_exempt
def payment_cancel(request):
    return render(request, 'payment/cancel.html')


def payment_process(request):
    order_id            = request.session.get('order_id')
    order               = get_object_or_404(Order, id=order_id)
    host                = request.get_host()
    paystack_total      = int(order.get_total_cost() * 100)
    data_key            = settings.PAYSTACK_PUBLIC_KEY
    data_email          = order.email
    return_url          = 'http://{}{}'.format(host, reverse('payment:payment-done'))

    context = {
        'order': order,
        'paystack_total': paystack_total,
        'data_key': data_key,
        'data_email': data_email,
        'return_url': return_url
    }
    return render(request, 'payment/process.html', context)
