from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
from apps.order.models import Coupon, OrderItem, Order


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code', 'amount', 'type', 'str_date', 'end_date', 'is_active']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'unit', 'qty', 'price']


class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['code', 'customer', 'amount', 'coupon', 'discount', 'total', 'date', 'status', 'payment',
                  'payment_type', 'tnx_id', 'order_item']
