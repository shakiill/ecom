from django.contrib import admin

# Register your models here.
from django.contrib.admin import TabularInline

from apps.order.models import Coupon, OrderItem, Order


class OrderItemInline(TabularInline):
    model = OrderItem
    fields = ['product', 'unit', 'qty', 'price']
    show_change_link = True
    extra = 0
    fk_name = "order"


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline, ]
    model = Order
    list_display = ['code', 'customer', 'total', 'payment']
    # list_filter = ['order__order__buyer', 'status', 'is_received']


admin.site.register(Coupon)
admin.site.register(Order, OrderAdmin)
