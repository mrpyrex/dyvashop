from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    order       = Order.objects.get(id=order_id)
    subject     = 'Order nr. {}'.format(order_id)
    message     = 'Dear {}, \n\n You have sucessfully placed an order. Your order id is {}.'.format(first_name, order_id)
    mail_sent   = send_mail(subject, message, 'order@dyvas.com', [order.email])
    return mail_sent