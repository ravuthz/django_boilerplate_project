from django.contrib import admin

from apps.carts.models import Cart, CartItem
from core.admins import CoreModelAdmin, CoreTabularInlineAdmin
from core.constants import date_fields


class CartItemAdminInline(CoreTabularInlineAdmin):
    model = CartItem
    fields = (
        'product',
        'cart',
        'price',
        'quantity',
        'amount',
    )
    list_display = (
                       'id',
                       'product',
                       'cart',
                       'price',
                       'quantity',
                       'amount',
                   ) + date_fields
    readonly_fields = ('amount',)

    def amount(self, obj):
        return float(obj.price) * int(obj.quantity)


@admin.register(Cart)
class CartModelAdmin(CoreModelAdmin):
    list_display = (
                       'id',
                       'customer',
                       'slug',
                       'code',
                       'desc',
                   ) + date_fields

    list_filter = (
                      'customer',
                      'is_removed',
                  ) + date_fields

    search_fields = ('slug',)
    date_hierarchy = 'created_at'

    inlines = (CartItemAdminInline,)


@admin.register(CartItem)
class CartItemModelAdmin(CoreModelAdmin):
    list_display = (
                       'id',
                       'product',
                       'cart',
                       'price',
                       'quantity',
                       'amount',
                   ) + date_fields

    list_filter = (
                      'cart',
                      'product',
                      'is_removed',
                  ) + date_fields

    date_hierarchy = 'created_at'
