from django.contrib import admin

from apps.orders.models import Order, OrderItem
from core.admins import CoreTabularInlineAdmin, CoreModelAdmin
from core.constants import date_fields


class OrderAdminInline(CoreTabularInlineAdmin):
    model = OrderItem
    fields = (
        'product',
        'price',
        'quantity',
        'amount',
        'discount',
    )
    list_display = (
                       'id',
                       'order',
                       'product',
                       'price',
                       'quantity',
                       'amount',
                       'discount',
                   ) + date_fields


@admin.register(Order)
class OrderModelAdmin(CoreModelAdmin):
    # payment_type ( Cash, Credit, Cheque )
    # payment_status ( Full, Advance, No Payment )
    list_display = (
                       'id',
                       'customer',
                       'slug',
                       'code',
                       'desc',
                       'payment_type',
                       'payment_status',

                   ) + date_fields

    list_filter = (
                      'customer',
                      'is_removed',
                  ) + date_fields

    search_fields = ('slug',)
    date_hierarchy = 'created_at'
    inlines = (OrderAdminInline,)


@admin.register(OrderItem)
class OrderItemModelAdmin(CoreModelAdmin):
    list_display = (
                       'id',
                       'order',
                       'product',
                       'price',
                       'quantity',
                       'amount',
                       'discount',
                   ) + date_fields

    list_filter = (
                      'order',
                      'product',
                      'is_removed',
                  ) + date_fields

    date_hierarchy = 'created_at'
