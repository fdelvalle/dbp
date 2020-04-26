from django.contrib import admin

from orders.models import Order, OrderItem
from products.admin import SkuInline


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInLine]
