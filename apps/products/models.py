from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.constants import tb_prefix
from core.models import BaseSlugName, BaseModel, BaseCodeDesc, BasePerson


class Category(BaseModel, BaseSlugName):
    class Meta:
        db_table = tb_prefix + "category"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["id"]

    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, default=None, blank=True, null=True
    )


class Product(BaseModel, BaseSlugName):
    class Meta:
        db_table = tb_prefix + "product"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["id"]

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=None, blank=False, null=False
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, null=False
    )
    quantity = models.PositiveIntegerField(
        default=0, blank=False, null=False
    )


class ProductVariant(BaseModel, BaseCodeDesc):
    class Meta:
        db_table = tb_prefix + "product_variant"
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Products Variants")
        ordering = ["id"]

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=None, null=False
    )
    value = models.TextField(
        max_length=255, null=True
    )
