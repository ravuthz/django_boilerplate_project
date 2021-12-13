from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.products.models import Product
from core.constants import tb_prefix
from core.models import BaseModel, BaseCodeDesc


class Cart(BaseModel, BaseCodeDesc):
    class Meta:
        db_table = tb_prefix + "cart"
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")
        ordering = ["id"]

    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=False
    )


class CartItem(BaseModel):
    class Meta:
        db_table = tb_prefix + "cart_item"
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Carts Items")
        ordering = ["id"]

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, default=None, null=False
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=None, null=False
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, null=False
    )
    quantity = models.PositiveIntegerField(
        default=0, blank=False, null=False
    )
    amount = models.PositiveIntegerField(
        default=0, blank=False, null=False
    )
