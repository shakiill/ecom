from django.db import models

# Create your models here.
from django.db.models import SET_NULL

from apps.account.models import Customer
from apps.product.models import Product


class Order(models.Model):
    class OrderChoices(models.IntegerChoices):
        PENDING = 1, 'Pending'
        IN_PROCESS = 2, 'In Process'
        DELIVERED = 3, 'Delivered'
        CANCEL = 4, 'Cancel'

    class PaymentChoices(models.IntegerChoices):
        PAID = 1, 'Paid'
        UN_PAID = 2, 'Un Paid'

    code = models.CharField(max_length=20, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=SET_NULL, null=True, blank=True, related_name='customer_order')
    amount = models.FloatField(default=0)
    coupon = models.CharField(max_length=50)
    discount = models.FloatField(default=0)
    total = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)
    status = models.SmallIntegerField(choices=OrderChoices.choices, default=1)
    payment = models.SmallIntegerField(choices=PaymentChoices.choices, default=1)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True, blank=True)
    unit = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    price = models.FloatField(default=0)
