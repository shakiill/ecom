from django.urls import path, include
from rest_framework import routers

from api.views import CouponViewSet, OrderViewSet, OrderItemViewSet

router = routers.DefaultRouter()
router.register(r'coupon', CouponViewSet, basename='coupon')
router.register(r'order_item', OrderItemViewSet, basename='order_item')
router.register(r'order', OrderViewSet, basename='order')
urlpatterns = [
    path('', include(router.urls)),
]
