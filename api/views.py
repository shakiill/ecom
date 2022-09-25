from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.serializers import CouponSerializer, OrderItemSerializer, OrderSerializer
from apps.order.models import Coupon, OrderItem, Order


class CouponViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    http_method_names = ['get', ]


class OrderItemViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
