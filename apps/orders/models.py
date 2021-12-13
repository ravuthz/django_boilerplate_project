from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
# apps.Order => created_by / updated_by = cashier_id / user_id
from model_utils import Choices

from apps.products.models import Product
from core.constants import tb_prefix
from core.models import BaseModel, BaseCodeDesc

PAYMENT_TYPE = Choices(
    ('CASH', _('Cash')),
    ('CREDIT', _('Credit')),
    ('CHEQUE', _('Cheque')),
)
PAYMENT_STATUS = Choices(
    ('FULL', _('Full')),
    ('ADVANCE', _('Advance')),
    ('NO_PAYMENT', _('No Payment')),
)


class Order(BaseModel, BaseCodeDesc):
    class Meta:
        db_table = tb_prefix + "order"
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ["id"]

    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=False
    )
    payment_type = models.CharField(choices=PAYMENT_TYPE, default=PAYMENT_TYPE.CASH, max_length=255)
    payment_status = models.CharField(choices=PAYMENT_STATUS, default=PAYMENT_STATUS.FULL, max_length=255)


class OrderItem(BaseModel):
    class Meta:
        db_table = tb_prefix + "order_item"
        verbose_name = _("Order Item")
        verbose_name_plural = _("Orders Items")
        ordering = ["id"]

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, default=None, null=False
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
    discount = models.PositiveIntegerField(
        default=0, blank=False, null=False
    )
